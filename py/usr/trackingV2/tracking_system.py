#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.audio.AudioControlSymetrix import SignalProbe


from usr.trackingV2.TrackSystem import TrackSystem
from usr.trackingV2.TrackQuuppa import TrackingEngineQuuppa

from usr.dev.dev import ipad_adm, quuppa_ip
from usr.trackingV2.TrackVars import trTagsProperties
from usr.cams.cam_control import roomCamProcessor
from usr.audio.audio_control import symetrix_proxy

quuppaTrEngn = TrackingEngineQuuppa(qpeServerIp=quuppa_ip.ip, qpeServerPort=quuppa_ip.port, qpePollInterval=2)

firstTagLabelId = 4500
for i in trTagsProperties:
    quuppaTrEngn.addTagLabel(tagId=i, UIHost=ipad_adm, lblId=firstTagLabelId + int(trTagsProperties[i]["micId"]))


roomTrackSystem = TrackSystem(quuppaTrEngn, roomCamProcessor)
roomTrackSystem.addStartStopBtn(uiHost=ipad_adm, btnId=4551)
roomTrackSystem.addModesBtn(uiHost=ipad_adm, btnPresetId=4552, btnZoneId=4553, btnCoordsId=4554)

for iTag in trTagsProperties:
    i = trTagsProperties[iTag]
    roomTrackSystem.addMicTagProbe(micId=i["micId"],
                                   presetId=i["presetId"],
                                   tagId=iTag,
                                   micRcId=i["rcId"],
                                   probeBtnId=i["btnProbeId"],
                                   micName=i["micName"],
                                   uiHost=ipad_adm,
                                   lblMicTrackNameId=i["lblMicNameId"],
                                   btnMicTrackStateId=i["btnStateId"],
                                   btnMicTrackModePresetId=i["btnModePreserId"],
                                   btnMicTrackModeZoneId=i["btnModeZoneId"],
                                   btnMicTrackModeCoordsId=i["btnModeCoordsId"])
