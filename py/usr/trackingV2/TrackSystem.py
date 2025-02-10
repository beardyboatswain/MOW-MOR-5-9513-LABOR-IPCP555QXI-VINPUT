#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Callable
import uuid

from extronlib import event
from extronlib.device import UIDevice
from extronlib.ui import Button, Label

import lib.utils.signals as signals
from lib.utils.CallbackObject import CallbackObject
from lib.var.states import sPressed, sReleased, sStates

from usr.trackingV2.TrackingEngineMeta import TrackingEngineMeta
from lib.camera.CameraControl import CameraControlProcessor

from lib.audio.AudioControlSymetrix import SignalProbe
from usr.audio.audio_control import symetrix_proxy
from usr.dev.dev import ipad_adm

from lib.utils.debugger import debuggerNet as debugger
from usr.trackingV2.TrackVars import TrackSystem_dbg
dbg = debugger(TrackSystem_dbg, __name__)


class TrackMic(object):
    trackModePreset = 1
    trackModeZone = 2
    trackModeCoords = 3
    trackModes = [trackModePreset, trackModeZone, trackModeCoords]

    trackStateOff = 0
    trackStateOn = 1
    trackStates = [trackStateOff, trackStateOn]

    def __init__(self,
                 micId: int,
                 presetId: int,
                 tagId: str,
                 micName: str = None,
                 uiHost: UIDevice = None,
                 lblMicTrackNameId: int = None,
                 btnMicTrackStateId: int = None,
                 btnMicTrackModePresetId: int = None,
                 btnMicTrackModeZoneId: int = None,
                 btnMicTrackModeCoordsId: int = None):
        self.micId = micId
        self.micName = micName
        self.presetId = presetId
        self.zoneId = presetId
        self.tagId = tagId
        self.tagData = None

        # включен или отключен трэкинг
        self.trackState = True
        # режим трэкинга
        self.trackMode = TrackMic.trackModePreset

        self.uiHost = uiHost
        self.lblMicName = None
        self.btnState = None
        self.btnModePreset = None
        self.btnModeZone = None
        self.btnModeCoords = None

        if lblMicTrackNameId:
            self.lblMicName = Label(self.uiHost, lblMicTrackNameId)
            if (self.micName):
                self.lblMicName.SetText(self.micName)
            else:
                self.lblMicName.SetText("M")
        if btnMicTrackStateId:
            self.btnState = Button(self.uiHost, btnMicTrackStateId)
            self.stateShowFb()
        if btnMicTrackModePresetId:
            self.btnModePreset = Button(self.uiHost, btnMicTrackModePresetId)
        if btnMicTrackModeZoneId:
            self.btnModeZone = Button(self.uiHost, btnMicTrackModeZoneId)
        if btnMicTrackModeCoordsId:
            self.btnModeCoords = Button(self.uiHost, btnMicTrackModeCoordsId)
        self.stateShowFb()
        self.modeShowFb()

        @event([self.btnModePreset, self.btnModeZone, self.btnModeCoords], sStates)
        def btnModeEventHandler(btn: Button, state: str):
            if (state == sPressed):
                if (btn.State == 0):
                    btn.SetState(1)
                elif (btn.State == 2):
                    btn.SetState(3)
            elif (state == sReleased):
                if (btn.State == 1):
                    btn.SetState(0)
                elif (btn.State == 3):
                    btn.SetState(2)
                if (btn == self.btnModePreset):
                    self.setTrakingMode(TrackMic.trackModePreset)
                elif (btn == self.btnModeZone):
                    self.setTrakingMode(TrackMic.trackModeZone)
                elif (btn == self.btnModeCoords):
                    self.setTrakingMode(TrackMic.trackModeCoords)

        @event(self.btnState, sStates)
        def btnStateEventHandler(btn: Button, state: str):
            if (state == sPressed):
                if (btn.State == 0):
                    btn.SetState(1)
                elif (btn.State == 2):
                    btn.SetState(3)
            elif (state == sReleased):
                if (btn.State == 1):
                    btn.SetState(0)
                elif (btn.State == 3):
                    btn.SetState(2)
                self.setTrackingState()

    def setData(self, tagData: dict) -> None:
        self.tagData = tagData
        # dbg.print("Mic {} (tag {}) - update data".format(self.micId, self.tagId))
        # dbg.print(self.tagData)

    def setTrackingState(self, state: int = None):
        if (state in TrackMic.trackStates):
            self.trackState = state
        else:
            self.trackState = not self.trackState
        self.stateShowFb()

    def setTrakingMode(self, mode: int):
        if (mode in TrackMic.trackModes):
            self.trackMode = mode
            self.modeShowFb()

    def stateShowFb(self):
        if self.btnState:
            self.btnState.SetState(2 if self.trackState else 0)
            self.modeShowFb()

    def modeShowFb(self):
        if self.btnModePreset:
            self.btnModePreset.SetState(0)
            if (self.trackMode == TrackMic.trackModePreset):
                self.btnModePreset.SetState(2)
        if self.btnModeZone:
            self.btnModeZone.SetState(0)
            if (self.trackMode == TrackMic.trackModeZone):
                self.btnModeZone.SetState(2)
        if self.btnModeCoords:
            self.btnModeCoords.SetState(0)
            if (self.trackMode == TrackMic.trackModeCoords):
                self.btnModeCoords.SetState(2)

    def getState(self) -> int:
        return self.trackState

    def getMode(self) -> int:
        return self.trackMode

    def getPreset(self) -> int:
        return self.presetId

    def getZone(self) -> int:
        return self.zoneId

    def getCoords(self) -> dict:
        return {"x": self.tagData.get("coords")[0],
                "y": self.tagData.get("coords")[1],
                "z": self.tagData.get("coords")[2]}


class TrackMicsQueue(object):
    def __init__(self):
        self.queue = list()
        self.callbackMethods = list()

    def addCallback(self, method: Callable, *args):
        self.callbackMethods.append({"id": uuid.uuid4(), "method": method, "args": args})

    def executeCallback(self, mic: TrackMic):
        for cm in self.callbackMethods:
            cm["method"](mic)

    def addMic(self, mic: TrackMic):
        if mic not in self.queue:
            self.queue.append(mic)
        else:
            while mic in self.queue:
                self.queue.remove(mic)
            self.queue.append(mic)
        self.executeCallback(self.getMic())
        self._printQueue()

    def removeMic(self, mic: TrackMic):
        while mic in self.queue:
            self.queue.remove(mic)
        self._printQueue()

    def getMic(self):
        if len(self.queue) > 0:
            self._printQueue()
            dbg.print("Top Mic {}".format(self.queue[-1]))
            return self.queue[-1]
        return None

    def _printQueue(self):
        dbg.print("Mig Queue {}".format(self.queue))


class TrackSystem(object):
    def __init__(self, engine: TrackingEngineMeta, camProcessor: CameraControlProcessor):
        # todo Вынести SymetrixProxy и SignalProbe в параметры конструктора, чтобы можно было добавить
        # todo любой детектор сигнала микрофона, который возвращает id канала микрофона и состояние
        # todo канала True/False

        # Traking on/off
        self.tracking = False

        # Buttons for turning on/off tracking
        self.trackingStartStopBtns = list()
        self.trackingModeBtns = list()

        # Tracking Engine, Quuppa or other
        self.engine = engine
        self.engine.addCallbackForUpdateTagData(self.engineCallback)
        self.engine.setTracking(self.tracking)

        # Camera Processor
        self.camProc = camProcessor

        self.mics = dict()
        self.tags = dict()
        self.queue = TrackMicsQueue()
        self.queue.addCallback(self.queueCallback)

        # Probe for mic fb (active/inactive)
        self.probes = dict()

    def addStartStopBtn(self, uiHost: UIDevice, btnId: int) -> None:
        self.trackingStartStopBtns.append(Button(uiHost, btnId))

        @event(self.trackingStartStopBtns, sStates)
        def trackingStartStopBtnsEventHandler(btn: Button, state: str) -> None:
            if (state == sPressed):
                if (btn.State == 0):
                    btn.SetState(1)
                elif (btn.State == 2):
                    btn.SetState(3)
            elif (state == sReleased):
                if (btn.State == 1):
                    btn.SetState(0)
                elif (btn.State == 3):
                    btn.SetState(2)
                self.setTracking()

        self.showStartStopTrackingBtnFb()

    def addModesBtn(self, uiHost: UIDevice, btnPresetId: int, btnZoneId: int, btnCoordsId: int) -> None:
        self.trackingModeBtns.append(Button(uiHost, btnPresetId))
        self.trackingModeBtns.append(Button(uiHost, btnZoneId))
        self.trackingModeBtns.append(Button(uiHost, btnCoordsId))

        @event(self.trackingModeBtns, sStates)
        def trackingModeBtnsEventHandler(btn: Button, state: str) -> None:
            if (state == sPressed):
                if (btn.State == 0):
                    btn.SetState(1)
                elif (btn.State == 2):
                    btn.SetState(3)
            elif (state == sReleased):
                if (btn.State == 1):
                    btn.SetState(0)
                elif (btn.State == 3):
                    btn.SetState(2)
                if (btn.ID == btnPresetId):
                    self.setTrakingModeForAllMics(TrackMic.trackModePreset)
                elif (btn.ID == btnZoneId):
                    self.setTrakingModeForAllMics(TrackMic.trackModeZone)
                elif (btn.ID == btnCoordsId):
                    self.setTrakingModeForAllMics(TrackMic.trackModeCoords)

    def setTracking(self, state: str = None) -> None:
        """
        Set the tracking state
        state: str = "On" or "Off"
        If None - toggle state
        """
        dbg.print("setTracking: {}".format(state))
        if (state == "On"):
            self.setTrackingOn()
        elif (state == "Off"):
            self.setTrackingOff()
        else:
            self.tracking = not self.tracking
            if self.tracking:
                self.setTrackingOn()
            else:
                self.setTrackingOff()

    def setTrackingOn(self) -> None:
        dbg.print("setTrackingOn")
        self.tracking = True
        # self.setTrakingStateForAllMics(TrackMic.trackStateOn)
        self.showStartStopTrackingBtnFb()
        self.engine.startTracking()

    def setTrackingOff(self) -> None:
        dbg.print("setTrackingOff")
        self.tracking = False
        # self.setTrakingStateForAllMics(TrackMic.trackStateOff)
        self.showStartStopTrackingBtnFb()
        self.engine.stopTracking()

    def setTrakingStateForAllMics(self, trackingState: int):
        if trackingState in TrackMic.trackStates:
            for iMic in self.mics:
                self.mics[iMic].setTrackingState(trackingState)

    def setTrakingModeForAllMics(self, trackingMode: int):
        if trackingMode in TrackMic.trackModes:
            for iMic in self.mics:
                self.mics[iMic].setTrakingMode(trackingMode)

    def showStartStopTrackingBtnFb(self) -> None:
        for iBtn in self.trackingStartStopBtns:
            iBtn.SetState(2 if self.tracking else 0)

    def addMicTagProbe(self, micId: int,
                       presetId: int,
                       tagId: str,
                       micRcId: int,
                       probeBtnId: int,
                       micName: str = None,
                       uiHost: UIDevice = None,
                       lblMicTrackNameId: int = None,
                       btnMicTrackStateId: int = None,
                       btnMicTrackModePresetId: int = None,
                       btnMicTrackModeZoneId: int = None,
                       btnMicTrackModeCoordsId: int = None) -> None:
        newMic = TrackMic(micId=micId,
                          presetId=presetId,
                          tagId=tagId,
                          micName=micName,
                          uiHost=uiHost,
                          lblMicTrackNameId=lblMicTrackNameId,
                          btnMicTrackStateId=btnMicTrackStateId,
                          btnMicTrackModePresetId=btnMicTrackModePresetId,
                          btnMicTrackModeZoneId=btnMicTrackModeZoneId,
                          btnMicTrackModeCoordsId=btnMicTrackModeCoordsId)
        # todo Смотри todo в конструкторе
        newProbe = SignalProbe(dev=symetrix_proxy, rcId=micRcId, ui=ipad_adm, btnId=probeBtnId)
        newProbe.addCallback(self.probeCallback)

        self.mics[micId] = newMic
        self.tags[tagId] = micId
        self.probes[micRcId] = {"mic": micId, "probe": newProbe}

    def engineCallback(self, tagsData: dict) -> None:
        # dbg.print("Tag data updated!")
        for iTag in tagsData:
            micId = self.tags[iTag]
            tagData = tagsData[iTag]
            self.mics[micId].setData(tagData)

    def queueCallback(self, mic: TrackMic) -> None:
        if (mic.getState() == TrackMic.trackStateOn):
            tMode = mic.getMode()

            if (tMode == TrackMic.trackModePreset):
                tPreset = mic.getPreset()
                self.camProc.trackPreset(tPreset)
                dbg.print("Mic {} Call preset {}".format(mic.micId, tPreset))
            elif (tMode == TrackMic.trackModeZone):
                tZone = mic.getZone()
                self.camProc.trackPreset(tZone)
                dbg.print("Mic {} Call zone preset {}".format(mic.micId, tZone))
            elif (tMode == TrackMic.trackModeCoords):
                tCoords = mic.getCoords()
                dbg.print("Mic {} Call coords {}".format(mic.micId, tCoords))
        else:
            dbg.print("Mic {} - Tracking stopped".format(mic.micId))

    # todo не опрашивать пробы постоянно
    def probeCallback(self, rcId: int, state: bool) -> None:
        dbg.print("MicProbe {} - {}".format(rcId, state))
        dbg.print("Mic {} {}".format(self.probes[rcId]["mic"], state))
        if state:
            self.queue.addMic(self.mics[self.probes[rcId]["mic"]])
        else:
            self.queue.removeMic(self.mics[self.probes[rcId]["mic"]])
