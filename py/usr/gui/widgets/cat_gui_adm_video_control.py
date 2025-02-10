#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.utils.system_init import InitModule

from lib.video.catVideoControl import cVideoOutput, cVideoOutputType
from usr.var.video_vars import VIDEO_OUTPUTS_XTP

from usr.dev.dev import ipad_adm

outButtons = []

for iO in VIDEO_OUTPUTS_XTP.keys():
    o = VIDEO_OUTPUTS_XTP.get(iO)
    newOutBtn = cVideoOutput(vName=o["name"].replace("\n", " "),
                             vOutNumber=o["out"],
                             vUIHost=ipad_adm,
                             vBtnBaseID=o["btnid"],
                             vType=o["type"])

InitModule(__name__)
