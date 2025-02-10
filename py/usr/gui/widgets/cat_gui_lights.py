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
from usr.var.debug_mode import cat_gui_lights_dbg
dbg = debugger.debugger(cat_gui_lights_dbg, __name__)

from usr.dev.dev import iPadUsrCat
from lib.var.states import *
import lib.utils.signals as signals


lightsValues={1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

btnLightTglID = 156
btnLightTgl = Button(iPadUsrCat, btnLightTglID)

def dmxSend():
    dbg.print("Lights = {}".format(lightsValues))
    cmd = "dmx=0"
    for i in lightsValues:
        cmd = cmd + ",{}".format(lightsValues[i])
    cmd = cmd + ',0\x0d'
    dbg.print("DMX send: {}".format(cmd))
    signals.emit('*', signal='dmx', params={'cmd':cmd})

def btnsUpdate():
    global lightsValues
    for i in lightsValues:
        if lightsValues[i] > 0:
            btnLightTgl.SetState(2)
            return
    btnLightTgl.SetState(0)



@event(btnLightTgl, sStates)
def btnLightTglEventHandler(btn, state):
    global lightsValues
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

        newValue = 255
        for i in lightsValues:
            if lightsValues[i] > 0:
                newValue = 0
                break
        
        for i in lightsValues:
            lightsValues[i] = newValue

        dmxSend()
        btnsUpdate()


@signals.on()
def dmxSignalHandler(signal, params):
    global lightsValues

    if (signal == "lights"):
        if(params.get('cmd') == 'alloff'):
            for i in lightsValues:
                lightsValues[i] = 0
            dmxSend()
            btnsUpdate()
        elif(params.get('cmd') == 'allon'):
            for i in lightsValues:
                lightsValues[i] = 255
            dmxSend()
            btnsUpdate()


# 156, 157