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
from usr.var.debug_mode import sys_scheduler_dbg
dbg = debugger.debugger(sys_scheduler_dbg, __name__)

import lib.utils.signals as signals
from lib.var.states import *

from usr.dev.dev import ipad_adm


btnSchedulerID = 1100
btnScheduler = Button(ipad_adm, btnSchedulerID)


def shutdownLightsSchedulerHandler():
    dbg.print('Time is coming! Scheduller will power off Lights!')
    signals.emit('*', signal='Lights', params={'ID':'All','cmd':'Off'})

def shutdownProjectorsSchedulerHandler():
    dbg.print('Time is coming! Scheduller will power off Projectors!')
    signals.emit('*', signal='Scheduler', params={'cmd':'Power', 'action':'Off'})

def schedulerRun(clock, dt):
    shutdownProjectorsSchedulerHandler()
    shutdownLightsSchedulerHandler()


shutdownProjectorsScheduler = Clock(['22:00:00'], None, schedulerRun)
shutdownProjectorsScheduler.SetDays(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
shutdownProjectorsScheduler.Enable()
if (shutdownProjectorsScheduler.State == 'Enabled'):
    btnScheduler.SetState(1)
else:
    btnScheduler.SetState(0)


def toggleScheduler():
    if (shutdownProjectorsScheduler.State == 'Enabled'):
        shutdownProjectorsScheduler.Disable()
    else:
        shutdownProjectorsScheduler.Enable()
    if (shutdownProjectorsScheduler.State == 'Enabled'):
        btnScheduler.SetState(1)
    else:
        btnScheduler.SetState(0)
    


@event(btnScheduler, sStates)
def btnSchedulerEventHandler(btn, state):
    if (state == sPressed):
        if (btn.State == 0):
            btn.SetState(2)
        elif (btn.State == 1):
            btn.SetState(3)
    elif (state == sReleased):
        if (btn.State == 2):
            btn.SetState(0)
        elif (btn.State == 3):
            btn.SetState(1)
        toggleScheduler()

shutdownProjectorsScheduler.Enable()
if (shutdownProjectorsScheduler.State == 'Enabled'):
    btnScheduler.SetState(1)
else:
    btnScheduler.SetState(0)
dbg.print("Scheduler is {}". format(shutdownProjectorsScheduler.State))

def Initialize():
    dbg.print('Imported')

Initialize()
