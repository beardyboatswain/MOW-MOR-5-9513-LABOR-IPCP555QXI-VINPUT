#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

from lib.utils.system_init import InitModule
import lib.utils.signals as signals

from usr.tracking.trackSystemVars import (trackZonesProperties,
                                          micHeight,
                                          trackCamProperties,
                                          trackTagsProperties,)

from usr.tracking.trackSystemTrackSpace import TrackZone, TrackSpace
from usr.tracking.trackSystemTagManager import TagManager, TrackMode


from lib.utils.debugger import debuggerNet as debugger
from usr.var.debug_mode import track_system_dbg
dbg = debugger(track_system_dbg, __name__)

trackSpace = TrackSpace(17000, 12310, 3200)

zonesFile = open(".\\py\\quuppa\getProjectInfo_Zones.json", "r")
zones = json.load(zonesFile)

print(zones)

for iZone in zones:
    print(iZone)
    print(zones.get(iZone).get("name"))
    print(tuple(zones.get(iZone).get("p1")))
    print(tuple(zones.get(iZone).get("p2")))
    trackSpace.addZone(
        TrackZone(
            zoneID=iZone,
            zoneName=zones.get(iZone).get("name"),
            cameraID=trackZonesProperties[zones.get(iZone).get("name")]["camID"],
            p1=tuple(zones.get(iZone).get("p1")),
            p2=tuple(zones.get(iZone).get("p2")),
            zoneHeightOffset=trackZonesProperties[zones.get(iZone).get("name")]["camID"]
        )
    )

trackSpace.setMicHeight(micHeight)
trackSpace.setTracking(True)


for iCam in trackCamProperties:
    trackSpace.PTZCalc.addCamera(
        room=1,
        cameraID=iCam,
        direction=trackCamProperties.get(iCam).get("direction"),
        position=trackCamProperties.get(iCam).get("coords"),
    )


trackTags = TagManager()
for iTag in trackTagsProperties:
    trackTags.registerTag(
        tagID=iTag,
        micID=trackTagsProperties.get(iTag).get("micID"),
        micPreset=trackTagsProperties.get(iTag).get("presetID"),
        tagName=trackTagsProperties.get(iTag).get("tagName"),
        micMode=TrackMode.TrackCoord,
    )

dbg.print("ALL TAGs: \n{}".format(trackTags))


@signals.on()
def trackSystemSignalHandler(signal, params):
    if (signal == "quuppa") and (params["Cmd"] == "NewPosition"):
        trackTags.setTag(
            tagID=params["Id"],
            tagName=params["Name"],
            tagPosition=params["Position"],
            tagSmoothpos=params["SmoothedPosition"],
        )
    elif signal == "tracking":
        dbg.print("SIG<{}> PARA<{}>".format(signal, params))
        if (params["Cmd"] == "Tracking") and (params["Action"] == "Tgl"):
            # вкл или выкл автотрэкинг и сразу отвечаем
            newTrackingState = trackSpace.tglTracking()
            signals.emit(
                "gui_tracking",
                signal="tracking",
                params={
                    "Cmd": "Tracking_fb",
                    "Action": ("On" if newTrackingState else "Off"),
                },
            )
            # отключаем запросы к серверу, чтобы не донимать его
            signals.emit(
                "dev_quuppa",
                signal="tracking",
                params={
                    "Cmd": "Tracking_fb",
                    "Action": ("On" if newTrackingState else "Off"),
                },
            )

    elif (signal == "mxwapt8") or (signal == "ulxd"):
        # 1-8 - MXW
        # 11-16 - ULXD
        dbg.print("SIG<{}> PARA<{}>".format(signal, params))
        dbg.print("MIC<{}> {}".format(params["Mic"], params["State"]))
        if params["State"] == "On":
            trackSpace.queueAddMic(params.get("Mic"))
        elif params["State"] == "Off":
            trackSpace.queueRemoveMic(params.get("Mic"))
        # !!! проверить, трекаем по пресету или по координатам
        tagCur = trackTags.getTag(micID=trackSpace.queueGetMic())

        dbg.print("------------ Mic <{}>".format(tagCur))
        if tagCur and trackSpace.getTracking():
            if tagCur["track_mode"] == TrackMode.TrackPreset:
                # трекаем по пресету
                dbg.print("To preset!")
                dbg.print(
                    "Mic <{}>, mode <{}> - preset <{}>".format(
                        tagCur["mic"], tagCur["track_mode"], tagCur["preset"]
                    )
                )
                signals.emit(
                    "dev_cameras",
                    signal="cam_preset",
                    params={"action": "Call", "preset": tagCur["preset"]},
                )
        else:
            # трекаем по координатам
            dbg.print("To coordinates!")
            trackSpace.trackTag(
                2520, trackTags.getTagCoordinatesByMic(trackSpace.queueGetMic())
            )


InitModule(__name__)
