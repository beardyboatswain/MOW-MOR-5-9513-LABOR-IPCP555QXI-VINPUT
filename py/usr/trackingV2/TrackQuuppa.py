#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import urllib.error
import urllib.request

from typing import Callable

from extronlib.system import Timer
from extronlib.device import UIDevice
from extronlib.ui import Label

import lib.utils.signals as signals

from usr.dev.dev import quuppa_ip, ipad_adm

from usr.trackingV2.TrackingEngineMeta import TrackingEngineMeta
from usr.trackingV2.TrackVars import trTagsProperties

from lib.utils.debugger import debuggerNet as debugger
from usr.trackingV2.TrackVars import trackQuuppa_dbg
dbg = debugger(trackQuuppa_dbg, __name__)


class TrackingEngineQuuppa(TrackingEngineMeta):
    def __init__(self, qpeServerIp: str, qpeServerPort: int, qpePollInterval: int = 1) -> None:
        super().__init__()

        self.serverIp = qpeServerIp
        self.serverPort = qpeServerPort
        self.pollInterval = qpePollInterval

        self.tags = dict()
        self.tagsFbData = dict()
        self.labels = dict()

        self.pollTimer = Timer(self.pollInterval, self.tagPollTimerHandler)

    def tagPollTimerHandler(self, timerName: str, timerCount: int) -> None:
        try:
            resp = urllib.request.urlopen("http://{}:{}/qpe/getTagPosition?version=2".format(quuppa_ip.ip, quuppa_ip.port))

            quuppaAnswer = resp.read()
            quuppaTags = json.loads(quuppaAnswer.decode("utf-8"))

            # dbg.print("Request: {} - {}".format(timerName, timerCount))

            for iTag in quuppaTags["tags"]:
                for i in range(0, len(iTag["position"])):
                    iTag["position"][i] *= 1000
                for i in range(0, len(iTag["smoothedPosition"])):
                    iTag["smoothedPosition"][i] *= 1000

                tagName = iTag["name"]
                tagId = iTag["id"]
                tagPosition = iTag["position"]
                tagSmoothedPosition = iTag["smoothedPosition"]
                tagZones = iTag["zones"]

                tagStoreData = {"name": tagName,
                                "id": tagId,
                                "position": tagPosition,
                                "smoothedPosition": tagSmoothedPosition,
                                "zones": tagZones}

                tagDataForCallback = {"id": tagStoreData["id"],
                                      "name": tagStoreData["name"],
                                      "zone": tagStoreData["zones"][0]["name"],
                                      "coords": (tagStoreData["smoothedPosition"][0],
                                                 tagStoreData["smoothedPosition"][1],
                                                 tagStoreData["smoothedPosition"][2])}

                if (tagId in trTagsProperties.keys()):
                    # dbg.print("ID[{}] NAME[{}] POSITION[{}] SMOOTHPOS[{}]".format(tagId,
                    #                                                               tagName,
                    #                                                               tagPosition,
                    #                                                               tagSmoothedPosition))

                    self.tags[tagId] = tagStoreData
                    self.tagsFbData[tagId] = tagDataForCallback

                self.updateTag(tagId)

                signals.emit("*",
                             signal="quuppa",
                             params={"Cmd": "NewPosition",
                                     "Id": tagId,
                                     "Name": tagName,
                                     "Position": tagPosition,
                                     "SmoothedPosition": tagSmoothedPosition})

        except BaseException as err:
            dbg.print("Error while requsing tag data: {}".format(err))

        self.executeCallbackForUpdateTagData()

    def updateTag(self, tagId: str) -> None:
        self.updateLabel(tagId)

    def updateLabel(self, tagId: str) -> None:
        # log_msg = "Updating data for Tag<{}> ".format(tagId)
        if (tagId in self.labels.keys()):
            newData = "{} ({})".format(self.tags[tagId].get("name"), self.tags[tagId].get("smoothedPosition"))
            self.labels[tagId].SetText(newData)
        #     log_msg += "on Label<{}>".format(self.labels[tagId].ID)
        # dbg.print(log_msg)

    def addTagLabel(self, tagId: str, UIHost: UIDevice, lblId: int, ) -> None:
        self.labels[tagId] = Label(UIHost, lblId)

    def addCallbackForUpdateTagData(self, fbCallbackFunction: Callable[[dict,], None]):
        if callable(fbCallbackFunction):
            self.fbCallbackFunctions.append(fbCallbackFunction)
        else:
            raise TypeError("Param 'fbCallbackFunction' is not Callable")

    def executeCallbackForUpdateTagData(self):
        dbg.print("Execute callbacks")
        for iFunc in self.fbCallbackFunctions:
            iFunc(self.tagsFbData)

    def startTracking(self) -> None:
        dbg.print("startTracking")
        self.pollTimer.Restart()

    def stopTracking(self) -> None:
        dbg.print("stopTracking")
        self.pollTimer.Stop()

    def setTracking(self, state: bool) -> None:
        if state:
            self.startTracking()
        else:
            self.stopTracking()
