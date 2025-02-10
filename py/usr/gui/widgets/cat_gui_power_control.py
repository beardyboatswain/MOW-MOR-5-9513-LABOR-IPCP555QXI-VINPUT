#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from extronlib import event, Version
from extronlib.device import eBUSDevice, ProcessorDevice, UIDevice
from extronlib.interface import (CircuitBreakerInterface, ContactInterface,
    DigitalInputInterface, DigitalIOInterface, EthernetClientInterface,
    EthernetServerInterfaceEx, FlexIOInterface, IRInterface, PoEInterface,
    RelayInterface, SerialInterface, SWACReceptacleInterface, SWPowerInterface,
    VolumeInterface)
from extronlib.ui import Button, Knob, Label, Level
from extronlib.system import Clock, MESet, Timer, Wait

import lib.utils.signals as signals

import lib.utils.debugger as debugger
from usr.var.debug_mode import gui_power_control_dbg
dbg = debugger.debugger(gui_power_control_dbg, __name__)

from cat_DevicePower import CatDevicePower, CatMainPower, CatDevicePowerMultiBtn, CatMainPowerMultiButton
from usr.dev.dev import iPadUsrCat, ipad_adm, ipad_usr
# from cat_dev_proxy import proj1Proxy, proj2Proxy, lcd1Proxy, lcd2Proxy, lcd3Proxy, lcd4Proxy, lcd5Proxy, lcd6Proxy
from cat_dev_proxy import lcd1Proxy, lcd2Proxy, lcd3Proxy, lcd4Proxy, lcd5Proxy, lcd6Proxy


# --- Show Controls ----------------------------------------------------------------
powerPPs = ["201_ProjectorLeft_Power_PP", 
            "202_ProjectorRight_Power_PP", 
            "203_Lcd1_ToStageLeft_Power_PP", 
            "204_Lcd2_ToHallLeft_Power_PP", 
            "205_Lcd3_ToStageRight_Power_PP",
            "206_Lcd4_ToHallRight_Power_PP",
            "207_Lcd5_ChatHall_Power_PP", 
            "208_Lcd6_ChatStage_Power_PP",
            "209_Main_Power_PP"]


for ppage in powerPPs:
    iPadUsrCat.ShowPopup(ppage)
    #iPadAdm.ShowPopup(ppage)

# proj1Power = CatDevicePowerMultiBtn(proj1Proxy, "Проектор левый")
# proj1Power.setMechanic(iPadUsrCat, devNameLblID=101, tglBtnID=102)
# proj1Power.setMechanic(iPadUsr, tglBtnID=1103, probeBtnID=1141)
# proj1Power.setMechanic(iPadAdm, tglBtnID=1103, probeBtnID=1141)

# proj2Power = CatDevicePowerMultiBtn(proj2Proxy, "Проектор правый")
# proj2Power.setMechanic(iPadUsrCat, devNameLblID=107, tglBtnID=108)
# proj2Power.setMechanic(iPadUsr, tglBtnID=1106, probeBtnID=1143)
# proj2Power.setMechanic(iPadAdm, tglBtnID=1106, probeBtnID=1143)

lcd1Power = CatDevicePowerMultiBtn(lcd1Proxy, "ЖК, левая на сцену")
lcd1Power.setMechanic(iPadUsrCat, devNameLblID=113, tglBtnID=114)
lcd1Power.setMechanic(ipad_adm, tglBtnID=1109)
                     
lcd2Power = CatDevicePowerMultiBtn(lcd2Proxy, "ЖК, левая в зал")
lcd2Power.setMechanic(iPadUsrCat, devNameLblID=119, tglBtnID=120)
lcd2Power.setMechanic(ipad_adm, tglBtnID=1112)

lcd3Power = CatDevicePowerMultiBtn(lcd3Proxy, "ЖК, правая на сцену")
lcd3Power.setMechanic(iPadUsrCat, devNameLblID=125, tglBtnID=126)
lcd3Power.setMechanic(ipad_adm, tglBtnID=1115)
                                    
lcd4Power = CatDevicePowerMultiBtn(lcd4Proxy, "ЖК, правая в зал")
lcd4Power.setMechanic(iPadUsrCat, devNameLblID=131, tglBtnID=132)
lcd4Power.setMechanic(ipad_adm, tglBtnID=1118)

lcd5Power = CatDevicePowerMultiBtn(lcd5Proxy, "ЖК, чат в зале")
lcd5Power.setMechanic(iPadUsrCat, devNameLblID=137, tglBtnID=138)
lcd5Power.setMechanic(ipad_adm, tglBtnID=1121)

lcd6Power = CatDevicePowerMultiBtn(lcd6Proxy, "ЖК, чат на сцене")
lcd6Power.setMechanic(iPadUsrCat, devNameLblID=143, tglBtnID=144)
lcd6Power.setMechanic(ipad_adm, tglBtnID=1124)


spinnerBtnID = 4
powerOffPageName = "000_Start_P"
powerOnPageName = "100_Home_P"


from usr.dev.dev import roomkit

mainPower = CatMainPowerMultiButton(devName="Питание зала")
mainPower.setMechanic(iPadUsrCat, devNameLblID=191, tglBtnID=192, stateLblID=193, powerOffPageName=powerOffPageName, powerOnPageName=powerOnPageName)
# mainPower.devices = proj1Proxy
# mainPower.devices = proj2Proxy
mainPower.devices = lcd1Proxy
mainPower.devices = lcd2Proxy
mainPower.devices = lcd3Proxy
mainPower.devices = lcd4Proxy
mainPower.devices = lcd5Proxy
mainPower.devices = lcd6Proxy

@signals.on()
def roomkitSignalsHandler(signal, params):

    if ((signal == 'roomkit_fb') and (params.get('cmd') == 'Standby') and (params.get('Action') == 'rfb')):
        dbg.print('SIG [{}]  PARA [{}]'.format(signal, params))
        if (params.get('state') ==  'Deactivate'):
            if (mainPower._power == 'Off'):
                mainPower.powerOn()
        elif (params.get('state') ==  'Activate'):
            if (mainPower._power == 'On'):
                mainPower.powerOff()


mainPowerLcds = CatMainPowerMultiButton(devName="ЖК-панели")
mainPowerLcds.setMechanic(ipad_usr, tglBtnID=1127)
mainPowerLcds.setMechanic(ipad_adm, tglBtnID=1127)
mainPowerLcds.devices = lcd1Proxy
mainPowerLcds.devices = lcd2Proxy
mainPowerLcds.devices = lcd3Proxy
mainPowerLcds.devices = lcd4Proxy
mainPowerLcds.devices = lcd5Proxy
mainPowerLcds.devices = lcd6Proxy


mainLeftProjector = CatMainPowerMultiButton(devName="Экран левый")
mainLeftProjector.setMechanic(iPadUsrCat, devNameLblID=150, tglBtnID=151)
mainLeftProjector.setMechanic(ipad_usr, tglBtnID=1103)
# mainLeftProjector.devices = proj1Proxy
mainLeftProjector.devices = lcd3Proxy
mainLeftProjector.devices = lcd4Proxy

mainRightProjector = CatMainPowerMultiButton(devName="Экран правый")
mainRightProjector.setMechanic(iPadUsrCat, devNameLblID=152, tglBtnID=153)
mainRightProjector.setMechanic(ipad_usr, tglBtnID=1106)
# mainRightProjector.devices = proj2Proxy
mainRightProjector.devices = lcd1Proxy
mainRightProjector.devices = lcd2Proxy

mainChatLcd = CatMainPowerMultiButton(devName="ТВ с чатом")
mainChatLcd.setMechanic(iPadUsrCat, devNameLblID=154, tglBtnID=155)
mainChatLcd.devices = lcd5Proxy
mainChatLcd.devices = lcd6Proxy


# --- deprecated ------------------------------------------------------------------------

@signals.on()
def powerSignalHandler(signal, params):
    if (signal == 'Scheduler'):
        if (params.get('cmd') == 'Power') and params.get('action'):
            mainPower.powerSet(params.get('action'))

signals.emit('*', signal='Scheduler', params={'cmd':'Power', 'action':'On'})

def Initialize():
   print("<{}> imported!".format(__name__))

Initialize()
