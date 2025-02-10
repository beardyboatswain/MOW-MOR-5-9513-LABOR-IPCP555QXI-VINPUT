from extronlib import event, Version
from extronlib.device import eBUSDevice, ProcessorDevice, UIDevice
from extronlib.interface import (CircuitBreakerInterface, ContactInterface,
    DigitalInputInterface, DigitalIOInterface, EthernetClientInterface,
    EthernetServerInterfaceEx, FlexIOInterface, IRInterface, PoEInterface,
    RelayInterface, SerialInterface, SWACReceptacleInterface, SWPowerInterface,
    VolumeInterface)
from extronlib.ui import Button, Knob, Label, Level
from extronlib.system import Clock, MESet, Timer, Wait, File

from lib.utils.debugger import debugger
from usr.var.debug_mode import sys_scripts_dbg
dbg = debugger(sys_scripts_dbg, __name__)

from lib.var.states import *
import lib.utils.signals as signals
import json

from gui_scripts import scriptsNumber

scripts = {}
cVideoTies = {}

tagVideo = 'video'
tagAudio = 'audio'
scriptTags = [tagAudio, tagVideo]

# file ________________________________________________________________________S
def saveToFile():
    global scripts
    try:
        fileForStore = File("scripts.json", "w")
        json.dump(scripts, fileForStore)
    except BaseException as err:
        print("Save scripts error: {}".format(err))
    finally:
        fileForStore.close()

def loadFromFile(): 
    global scripts
    try:
        fileForLoad = File("scripts.json", "r")
        scripts = json.load(fileForLoad)
        dbg.print('Load scripts[]: {}'.format(scripts))
    except BaseException as err:
        print("Load scripts error: {}".format(err))
    finally:
        fileForLoad.close()

if (File.Exists("scripts.json")):
    loadFromFile()
else:
    for i in range(1,scriptsNumber + 1):
        scripts[i] = {}
        for t in scriptTags:
            scripts[i].update({t:{}})
    dbg.print('generated: {}'.format(scripts))
    saveToFile()

# _____________________________________________________________________________


def save(sID):
    global scripts, cVideoTies
    scripts[sID] = {}
    # save current states to script
    for i in scriptTags:
        if (i == tagVideo):
            scripts[sID].update({i:cVideoTies.copy()})
        elif (i == tagAudio):
            scripts[sID].update({i:{}})
    saveToFile()

def call(sID):
    global scripts
    dbg.print('Call Script[{}]'.format(sID))
    
    if (sID in ['1','2','3','4','5','6']):
        # включаем проекторы
        # включаем все дисплеи
        signals.emit('*', signal='Scheduler', params={'cmd':'Power', 'action':'On'})

        for i in scripts[sID]:
            if (i == tagVideo):
                # processing video in script
                for out in scripts[sID][tagVideo]:
                    signals.emit('*', signal='video_sw', params={'input':scripts[sID][tagVideo][out], 'output':out})
                    dbg.print('Scripts [{}]: signal={}, params={}'.format(tagVideo, 'video_sw', {'input':scripts[sID][tagVideo][out], 'output':out}))
            elif (i == tagAudio):
                # processing audio in script
                pass
    elif (sID == '7'):
        # Сценарий выключения
        # выключаем проекторы
        # выключаем все дисплеи
        signals.emit('*', signal='Scheduler', params={'cmd':'Power', 'action':'Off'})
        
    if (sID == '6'):
        # если Хурал, то еще сбрасываем звуковые настройки
        signals.emit('*', signal='biamp_preset_recall', params={'Preset':'1'})

actions = {'Save':save, 'Call':call}

@signals.on()
def gefenFbSignalHandler(signal, params):
    global cVideoTies
    if (signal == 'av_videosw_fb'):
        dbg.print('Tie: out{} - in{}'.format(params['output'], params['input']))
        cVideoTies[params['output']] = params['input']
    elif (signal == 'script'):
        dbg.print('Signal={} Params={}'.format(signal, params))
        actions[params['Command']](params['Script ID'])

def Initialize():
    dbg.print("Imported!")

Initialize()
