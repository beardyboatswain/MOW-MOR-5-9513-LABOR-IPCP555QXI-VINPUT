#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from extronlib.system import Timer

from lib.utils.debugger import debugger
from usr.var.debug_mode import track_system_tag_manager_dbg
dbg = debugger(track_system_tag_manager_dbg, __name__)


class TrackMode:
    TrackOff = "TrackOff"
    TrackCoord = "TrackCoord"
    TrackPreset = "TrackPreset"


class TagManager(object):
    def __init__(self):
        self.tags = {}

    def registerTag(
        self,
        tagID: str,
        micID: int,
        micPreset: int = "None",
        tagName: str = "tagName",
        micMode: TrackMode = TrackMode.TrackCoord,
    ):
        self.tags[tagID] = {
            "mic": micID,
            "name": "None",
            "track": True,
            "point": "None",
            "preset": micPreset,
            "track_mode": micMode,
        }

    def __repr__(self):
        representation = ""
        for i in self.tags:
            representation += "\nID:{:12},  NAME:{:4}  MIC:{:2},  TR:{},  P:{}".format(
                i,
                self.tags[i]["name"],
                self.tags[i]["mic"],
                self.tags[i]["track"],
                self.tags[i]["point"],
            )
        return representation

    def setTag(self, tagID, tagName, tagPosition, tagSmoothpos):
        self.tags[tagID]["name"] = tagName
        self.tags[tagID]["point"] = (tagSmoothpos[0], tagSmoothpos[1], tagSmoothpos[2])
        # self.tags[tagID]['point'] = (tagPosition[0], tagPosition[1], tagPosition[2])
        dbg.print(
            "\nID:{:12},  NAME:{:4}  MIC:{:2},  TR:{},  P:{}".format(
                tagID,
                self.tags[tagID]["name"],
                self.tags[tagID]["mic"],
                self.tags[tagID]["track"],
                self.tags[tagID]["point"],
            )
        )

    def getTag(self, tagID=None, micID=None):
        dbg.print("getTag {}-{} from \n{}".format(tagID, micID, self.tags))
        if tagID:
            dbg.print("GET TAG by ID: {}".format(self.tags[tagID]))
            return self.tags[tagID]
        elif micID:
            for tag in self.tags:
                dbg.print("tag {}".format(self.tags[tag]))
                if self.tags[tag]["mic"] == micID:
                    dbg.print("GET TAG by MIC: {}".format(self.tags[tag]))
                    return self.tags[tag]
        else:
            dbg.print("NO TAG")
            return None

    def getTagCoordinatesByMic(self, micID):
        for i in self.tags:
            if self.tags[i]["mic"] == micID:
                return self.tags[i]["point"]
        return None
