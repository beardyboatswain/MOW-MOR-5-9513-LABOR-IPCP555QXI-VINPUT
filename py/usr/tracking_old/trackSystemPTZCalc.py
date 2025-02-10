#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import acos, degrees

from extronlib.system import Timer

from usr.tracking.trackSystemVars import x, y, z, d

from lib.utils.debugger import debugger
from usr.var.debug_mode import track_system_ptz_calc_dbg

dbg = debugger(track_system_ptz_calc_dbg, __name__)


class PTZCalc(object):
    def __init__(self, angleUnits: str = "DEG"):
        """
        angleUnits: str - "DEG" results in degrees, "RAD" results in radians
        """
        self.cams = {}
        # cams: dict - Camera Position Direction and Coordinates {'d': ("N"|"S"|"E"|"W"), 'x': 123, 'y':456, 'z':789}
        self.angleUnits = angleUnits
        # "DEG" results in degrees, "RAD" results in radians

    def printCamerasList(self):
        for room in self.cams:
            for camera in self.cams[room]:
                dbg.print(
                    "ROOM[{}] CAM[{}] - DIR[{}] POS[{:5},{:5},{:5}]".format(
                        room,
                        camera,
                        self.cams[room][camera][d],
                        self.cams[room][camera][x],
                        self.cams[room][camera][y],
                        self.cams[room][camera][z],
                    )
                )

    def addCamera(self, room: int, camera: int, direction: str, position: tuple):
        """
        Add camers to list of cameras.
        room: int - Room Number [412|413]
        camera: int - Camera Number [1|2|3|4]
        direction: str - Camera Direction ("N"|"S"|"E"|"W")
        position: tuple - Camera Position (x_pos, y_pos, z_pos)
        """
        if room not in self.cams.keys():
            self.cams[room] = {}
        if camera not in self.cams[room]:
            self.cams[room][camera] = {}
        self.cams[room][camera] = {
            d: direction,
            x: position[0],
            y: position[1],
            z: position[2],
        }

    def getCameraPosition(self, camera: tuple) -> dict:
        """
        Calc PTZ
        camera: tuple - Room and Camera numbers (room, camera)
        Returns -> dict - Cam Position Coordinates {'direction': ("N"|"S"|"E"|"W"),
                                                    'x_pos': x,
                                                    'y_pos': y,
                                                    'z_pos': z}
        """
        try:
            return self.cams[camera[0]][camera[1]]
        except BaseException as err:
            dbg.print("Error while getting camera data: {}".format(err))

    def calcPointForAllCameras(self, trackPoint: tuple) -> dict:
        """
        Calc PTZ for one Point and all Cameras
        """
        ptz = {}
        for room in self.cams:
            for camera in self.cams[room]:
                if room not in ptz.keys():
                    ptz[room] = {}
                if camera not in ptz[room].keys():
                    ptz[room][camera] = self.calcPoint((room, camera), trackPoint)
        dbg.print("POINT {}\nPTZs {}".format(trackPoint, ptz))
        return ptz

    def calcPoint(self, camera: tuple, trackPoint: tuple) -> dict:
        """
        Calc PTZ
        camera: tuple - Room and Camera numbers (room, camera)
        trackPoint: tuple - Track Point Coordinates (x, y, z)
        Returns -> dict - PTZ Coordinates {'pan':37, 'tilt':14, 'zoom':2530}
        """
        # exclude null devision exception
        try:
            cP = self.cams[camera[0]][camera[1]]
        except BaseException as err:
            dbg.print("Error while getting camera data: {}".format(err))

        tP = {
            x: (trackPoint[0] if cP[x] != trackPoint[0] else trackPoint[0] + 1),
            y: (trackPoint[1] if cP[y] != trackPoint[1] else trackPoint[1] + 1),
            z: (trackPoint[2] if cP[z] != trackPoint[2] else trackPoint[2] + 1),
        }

        dbg.print(
            "camera ({},{},{})\ttrack ({},{},{})".format(
                cP[x], cP[y], cP[z], tP[x], tP[y], tP[z]
            )
        )

        # tilt calculating
        tilt = acos(
            (((tP[x] - cP[x]) ** 2 + (tP[y] - cP[y]) ** 2) ** 0.5) / (
                ((tP[x] - cP[x]) ** 2 + (tP[y] - cP[y]) ** 2 + (tP[z] - cP[z]) ** 2)
                ** 0.5
            )
        )
        if tP[z] < cP[z]:
            tilt = -tilt

        # pan calculating
        if cP[d] == "N":
            C = {x: 0, y: 1}
            quater = cP[x] > tP[x]
        elif cP[d] == "S":
            C = {x: 0, y: -1}
            quater = cP[x] < tP[x]
        elif cP[d] == "E":
            C = {x: 1, y: 0}
            quater = cP[y] < tP[y]
        elif cP[d] == "W":
            C = {x: -1, y: 0}
            quater = cP[y] > tP[y]
        else:
            C = {x: 1, y: 0}
            quater = cP[y] < tP[y]

        T = {x: tP[x] - cP[x], y: tP[y] - cP[y]}
        pan = acos(
            (C[x] * T[x] + C[y] * T[y])
            / (((C[x] ** 2 + C[y] ** 2) ** 0.5) * ((T[x] ** 2 + T[y] ** 2) ** 0.5))
        )
        if quater:
            pan = -pan

        # zoom calculating
        zoom = (
            (tP[x] - cP[x]) ** 2 + (tP[y] - cP[y]) ** 2 + (tP[z] - cP[z]) ** 2
        ) ** 0.5

        dbg.print(
            "PTZ ({:.2f}°, {:.2f}°, {:.2f})".format(degrees(pan), degrees(tilt), zoom)
        )

        return (
            {"cam": camera, "pan": pan, "tilt": tilt, "zoom": zoom}
            if (self.angleUnits == "RAD")
            else {
                "cam": camera,
                "pan": round(degrees(pan)),
                "tilt": round(degrees(tilt)),
                "zoom": round(zoom),
            }
        )
