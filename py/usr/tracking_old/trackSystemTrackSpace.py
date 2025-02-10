#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from extronlib.system import Timer

# from trackSystemVars import *
import lib.utils.signals as signals
from trackSystemPTZCalc import PTZCalc

from usr.gui.cams.gui_cam_control import mainPreset

from lib.utils.debugger import debugger
from usr.var.debug_mode import track_system_track_space_dbg

dbg = debugger(track_system_track_space_dbg, __name__)


class PointManager(object):
    def __init__(self):
        pass


class TrackPoint(object):
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    def get(self):
        return self.x, self.y, self.z

    def getD(self):
        # return {x: self.x, y: self.y, z: self.z}
        return {"x": self.x, "y": self.y, "z": self.z}

    def set(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z


class TrackZone(object):
    def __init__(
        self,
        zoneID: int,
        zoneName: str,
        cameraID: int,
        p1: tuple,
        p2: tuple,
        zoneHeightOffset: int = 0,
    ):
        self.zoneID = zoneID
        self.zoneName = zoneName
        self.cameraID = cameraID
        self.x0 = p1[0]
        self.y0 = p1[1]
        self.x1 = p2[0]
        self.y1 = p2[1]
        self.zOffset = zoneHeightOffset

    def checkPoint(self, point: tuple) -> bool:
        """
        Check if the point - tuple (x,y) -  is inside of area or outside.
        Work only for rectangle areas.
        """
        return (self.x0 <= point[0] <= self.x1) and (self.y0 <= point[1] <= self.y1)

    def getCamera(self, point: tuple) -> int:
        """
        Return camera id if point - tuple (x,y) is inside of area, and 0 otherwise.
        """
        if self.checkPoint(point):
            return self.cameraID
        else:
            return 0

    def getHeightOffset(self):
        return self.zOffset

    def __repr__(self):
        return "ID<{}> CAM<{}> ({},{})-({},{})".format(
            self.zoneID, self.cameraID, self.x0, self.y0, self.x1, self.y1
        )

    def __str__(self):
        return "ID<{}> CAM<{}> ({:5},{:5})-({:5},{:5})".format(
            self.zoneID, self.cameraID, self.x0, self.y0, self.x1, self.y1
        )


class TrackSpace(object):
    def __init__(
        self, spaceLength: int, spaceWidth: int, spaceHeight: int, mode2d3d: str = "2d"
    ):
        """
        spaceLength: int - x axis
        spaceWidth: int - y axis
        spaceHeight: int - z axis
        mode2d3d: str - '2d' or '3d'
        """
        self.length = spaceLength
        self.width = spaceWidth
        self.height = spaceHeight
        self.zones = []
        self.tracking = False  # active or inactive tracking
        self.PTZCalc = PTZCalc("DEG")
        self.micHeight = 1500
        self.micQueue = []
        self.mode2d3d = mode2d3d

    def addZone(
        self, areaID=0, cameraID=0, x0=0, y0=0, x1=0, y1=0, height=0, area=None
    ):
        if (area is not None) and (type(area) is TrackZone):
            self.zones.append(area)
        else:
            self.zones.append(
                TrackZone(
                    zoneID=areaID,
                    cameraID=cameraID,
                    x0=x0,
                    y0=y0,
                    x1=x1,
                    y1=y1,
                    zoneHeightOffset=height,
                )
            )

    def __repr__(self):
        representation = "L:{}, W:{}, H:{}".format(self.length, self.width, self.height)
        for i in self.zones:
            representation += "\n" + str(i)
        return representation

    def checkPoint(self, point: tuple) -> bool:
        for area in self.zones:
            if area.checkPoint(point):
                return True
        return False

    def getCamera(self, point: tuple) -> int:
        for area in self.zones:
            if area.checkPoint(point):
                return area.getCamera(point)
        return 0

    def setTracking(self, tracking: bool):
        self.tracking = tracking
        dbg.print(
            "--- TRACKING {} --------------".format("ON" if self.tracking else "OFF")
        )
        if not self.tracking:
            self.micQueue = []

        signals.emit(
            "dev", signal="tracking", params={"Cmd": "Tracking", "Action": "Tgl"}
        )

    def tglTracking(self) -> bool:
        self.tracking = not self.tracking
        dbg.print(
            "--- TRACKING {} --------------".format("ON" if self.tracking else "OFF")
        )
        if not self.tracking:
            self.micQueue = []
        return self.tracking

    def getTracking(self) -> bool:
        return self.tracking

    def setMicHeight(self, height: int):
        if height >= 0:
            self.micHeight = height

    def checkTag(self, point):
        if self.tracking and self.checkPoint(point):
            return True
        else:
            return False

    def getZone(self, point: tuple) -> TrackZone:
        for a in self.zones:
            if a.checkPoint(point):
                return a
        return None

    def getTagPosition(self, point):
        if self.checkPoint(point):
            return (
                point[0],
                point[1],
                point[2] + self.getZone(point).getHeightOffset(),
            )

    def trackTag(self, room: int, tag: tuple):
        global mainPreset

        if self.tracking:
            if tag is not None:
                # point = (tag[0], tag[1], tag[2])
                # in 2d mode replace z-coordinate with micHeight
                if self.mode2d3d == "2d":
                    point = (tag[0], tag[1], self.micHeight)
                else:
                    point = (tag[0], tag[1], tag[2])

                if self.checkTag(point):
                    trackPoint = self.getTagPosition(point)
                    dbg.print("Try to track tag {} in room {}".format(trackPoint, room))
                    ptz = self.PTZCalc.calcPoint(
                        (room, self.getCamera(point)), trackPoint
                    )
                    dbg.print(
                        "SEND TO CAM {}: PTZ(pan:{:4}, tilt:{:4}, zoom:{:4})".format(
                            ptz["cam"], ptz["pan"], ptz["tilt"], ptz["zoom"]
                        )
                    )
                    signals.emit(
                        "dev_cameras",
                        signal="cam_position",
                        params={"Cmd": "Set", "PTZ": ptz},
                    )
            else:
                dbg.print("SEND TO CAM MAIN PRESET!!!!!!")
                # !!!
                # !!!signals.emit('*', signal='Camera', params={'action':'Preset', 'direction':'Call', 'preset':mainPreset})
                signals.emit(
                    "*",
                    signal="cam_preset",
                    params={"action": "Call", "preset": mainPreset},
                )

    def queueAddMic(self, mic):
        if mic not in self.micQueue:
            self.micQueue.append(mic)
        # self.micQueue.append(mic)
        dbg.print("Mig Queue {}".format(self.micQueue))

    def queueRemoveMic(self, mic):
        while mic in self.micQueue:
            self.micQueue.remove(mic)
        # if (mic in self.micQueue):
        #     self.micQueue.remove(mic)
        dbg.print("Mig Queue {}".format(self.micQueue))

    def queueGetMic(self):
        if len(self.micQueue) > 0:
            dbg.print("Mig Queue {}".format(self.micQueue))
            dbg.print("Top Mic {}".format(self.micQueue[-1]))
            return self.micQueue[-1]
        return None
