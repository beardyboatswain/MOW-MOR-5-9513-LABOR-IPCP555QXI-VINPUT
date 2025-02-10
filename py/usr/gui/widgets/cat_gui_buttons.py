#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from extronlib import event, Version
from extronlib.device import eBUSDevice, ProcessorDevice, UIDevice
from extronlib.interface import (CircuitBreakerInterface, ContactInterface,
    DigitalInputInterface, DigitalIOInterface, EthernetClientInterface,
    EthernetServerInterfaceEx, FlexIOInterface, IRInterface, PoEInterface,
    RelayInterface, SerialInterface, SWACReceptacleInterface, SWPowerInterface,
    VolumeInterface)
from extronlib.ui import Button, Knob, Label, Level, Slider
from extronlib.system import Clock, MESet, Timer, Wait


import lib.utils.debugger as debugger
from usr.var.debug_mode import gui_buttons_dbg
dbg = debugger.debugger(gui_buttons_dbg, __name__)

from lib.var.states import *
from usr.dev.dev import iPadUsrCat
import lib.utils.signals as signals




pp_111_Cam_Control_PP = "111_Cam_Control_PP"

pp110_Cam_Control_ShowPP_PP = "110_Cam_Control_ShowPP_PP"
pp112_Karaoke_PP = "112_Karaoke_PP"
pp113_AV_Preset1_PP = "113_AV_Preset1_PP"
pp114_AV_Preset2_PP = "114_AV_Preset2_PP"

staticPopups = [pp110_Cam_Control_ShowPP_PP, pp112_Karaoke_PP, pp113_AV_Preset1_PP]

for pp in staticPopups:
    iPadUsrCat.ShowPopup(pp)


lblLightAll = Label(iPadUsrCat, 11)
btnLightAll = Button(iPadUsrCat, 12)
lblLightAllValue = "Освещение сцены выключено"
btnLightAllValue = 0
lblLightAll.SetText(lblLightAllValue)
btnLightAll.SetState(btnLightAllValue)


@event(btnLightAll, sStates)
def btnLightAllEventHandler(btn, state):
    global lblLightAllValue, btnLightAllValue
    dbg.print("BTN={} STATE={}".format(btn.ID, state))

    if (state == sReleased):
        if (btnLightAllValue == 0):
            btnLightAllValue = 1
            lblLightAllValue = "Освещение сцены включено"
        elif (btnLightAllValue == 1):
            btnLightAllValue = 0
            lblLightAllValue = "Освещение сцены выключено"
        lblLightAll.SetText(lblLightAllValue)
        btnLightAll.SetState(btnLightAllValue)





# --- CAM -------------------------------------------------------------------------------
btnCamPPShow = Button(iPadUsrCat, 51)
btnCamPPClose = Button(iPadUsrCat, 52)

btnCamPPControl = [btnCamPPShow, btnCamPPClose]

@event(btnCamPPControl, sStates)
def btnCamPPControlEventHandler(btn, state):
    dbg.print("Btn [{}] - State [{}]".format(btn.Name, state))
   
    if (state == sPressed):
        btn.SetState(1)
    elif (state == sReleased):
        btn.SetState(0)
        if (btn == btnCamPPShow):
            iPadUsrCat.ShowPopup(pp_111_Cam_Control_PP)
        elif (btn == btnCamPPClose):
            iPadUsrCat.HidePopup(pp_111_Cam_Control_PP)  

# --- CAM PRESETS -----------------------------------------------------------------------
lblCamState = Label(iPadUsrCat, 53)
btnCamPresetStage = Button(iPadUsrCat, 54)
btnCamPresetHall = Button(iPadUsrCat, 55)

btnCamPresets = [btnCamPresetStage, btnCamPresetHall]

@event(btnCamPresets, sStates)
def btnCamPresetsEventHandler(btn, state):
    dbg.print("Btn [{}] - State [{}]".format(btn.Name, state))
   
    if (state == sPressed):
        btn.SetState(1)
    elif (state == sReleased):
        if (btn == btnCamPresetStage):
            signals.emit('*', signal='cam_preset', params={'action':'Call', 'preset':922})
            signals.emit(['trackSystem'], signal='tracking', params={'Cmd':'Tracking', 'Action':'Off'})
        elif (btn == btnCamPresetHall):
            signals.emit('*', signal='cam_preset', params={'action':'Call', 'preset':923})
            signals.emit(['trackSystem'], signal='tracking', params={'Cmd':'Tracking', 'Action':'Off'})
        @Wait(1)
        def btnWait():
            btn.SetState(0)



# --- SCRIPTS ---------------------------------------------------------------------------
btnScript1 = Button(iPadUsrCat, 61)
btnScript2 = Button(iPadUsrCat, 62)

btnScript = [btnScript1, btnScript2]

@event(btnScript, sStates)
def ParamsEventHandler(btn, state):
    dbg.print("Btn [{}] - State [{}]".format(btn.Name, state))
   
    if (state == sPressed):
        btn.SetState(1)
        if (btn == btnScript1):
            signals.emit('*', signal='script', params={'Command': 'Call', 'Script ID': str(6)})
        elif (btn == btnScript2):
            signals.emit('*', signal='script', params={'Command': 'Call', 'Script ID': str(2)})
    elif (state == sReleased):
        @Wait(1)
        def btnWait():
            btn.SetState(0)
        


# --- INIT ------------------------------------------------------------------------------


def Initialize():
   print("<{}> imported!".format(__name__))

Initialize()
