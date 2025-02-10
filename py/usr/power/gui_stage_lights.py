#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.utils.system_init import InitModule
from lib.lights.stage_lights_2 import (LightPowerProxy,
                                    LightPower,
                                    LightPowerGroup,
                                    LightPowerGroupUser)

from usr.dev.dev import lightshark, ipad_adm, ipad_usr


lightProxy = LightPowerProxy(lightshark)

lightGr01 = LightPower(dev=lightProxy, id="S/LS/Level/PB/1", onValue=255)
lightGr01.setMechanics(uiHost=ipad_adm, btnTglPowerID=971)

lightGr02 = LightPower(dev=lightProxy, id="S/LS/Level/PB/2", onValue=255)
lightGr02.setMechanics(uiHost=ipad_adm, btnTglPowerID=972)

lightGr03 = LightPower(dev=lightProxy, id="S/LS/Level/PB/3", onValue=255)
lightGr03.setMechanics(uiHost=ipad_adm, btnTglPowerID=973)

lightGr04 = LightPower(dev=lightProxy, id="S/LS/Level/PB/4", onValue=255)
lightGr04.setMechanics(uiHost=ipad_adm, btnTglPowerID=974)

lightGr05 = LightPower(dev=lightProxy, id="S/LS/Level/PB/5", onValue=255)
lightGr05.setMechanics(uiHost=ipad_adm, btnTglPowerID=975)

lightGr06 = LightPower(dev=lightProxy, id="S/LS/Level/PB/6", onValue=255)
lightGr06.setMechanics(uiHost=ipad_adm, btnTglPowerID=976)

lightGr11 = LightPower(dev=lightProxy, id="S/LS/Level/PB/11", onValue=76)
lightGr11.setMechanics(uiHost=ipad_adm, btnTglPowerID=961)

lightGr12 = LightPower(dev=lightProxy, id="S/LS/Level/PB/12", onValue=76)
lightGr12.setMechanics(uiHost=ipad_adm, btnTglPowerID=962)

lightGr13 = LightPower(dev=lightProxy, id="S/LS/Level/PB/13", onValue=76)
lightGr13.setMechanics(uiHost=ipad_adm, btnTglPowerID=963)

lightGr14 = LightPower(dev=lightProxy, id="S/LS/Level/PB/14", onValue=76)
lightGr14.setMechanics(uiHost=ipad_adm, btnTglPowerID=964)

lightGr15 = LightPower(dev=lightProxy, id="S/LS/Level/PB/15", onValue=76)
lightGr15.setMechanics(uiHost=ipad_adm, btnTglPowerID=965)

lightGr16 = LightPower(dev=lightProxy, id="S/LS/Level/PB/16", onValue=76)
lightGr16.setMechanics(uiHost=ipad_adm, btnTglPowerID=966)

lamps = LightPowerGroup()
lamps.setMechanics(uiHost=ipad_adm, btnTglPowerID=952)
lamps.addGroup(lightGr11)
lamps.addGroup(lightGr12)
lamps.addGroup(lightGr13)
lamps.addGroup(lightGr14)
lamps.addGroup(lightGr15)
lamps.addGroup(lightGr16)

projectors = LightPowerGroup()
projectors.setMechanics(uiHost=ipad_adm, btnTglPowerID=953)
projectors.addGroup(lightGr01)
projectors.addGroup(lightGr02)
projectors.addGroup(lightGr03)
projectors.addGroup(lightGr04)
projectors.addGroup(lightGr05)
projectors.addGroup(lightGr06)

alllights = LightPowerGroup()
alllights.setMechanics(uiHost=ipad_adm, btnTglPowerID=951)
alllights.addGroup(lightGr01)
alllights.addGroup(lightGr02)
alllights.addGroup(lightGr03)
alllights.addGroup(lightGr04)
alllights.addGroup(lightGr05)
alllights.addGroup(lightGr06)
alllights.addGroup(lightGr11)
alllights.addGroup(lightGr12)
alllights.addGroup(lightGr13)
alllights.addGroup(lightGr14)
alllights.addGroup(lightGr15)
alllights.addGroup(lightGr16)

alllights = LightPowerGroupUser()
alllights.setMechanics(uiHost=ipad_usr, btnTglPowerID=951)
alllights.addGroup(lightGr01)
alllights.addGroup(lightGr02)
alllights.addGroup(lightGr03)
alllights.addGroup(lightGr04)
alllights.addGroup(lightGr05)
alllights.addGroup(lightGr06)
alllights.addGroup(lightGr11)
alllights.addGroup(lightGr12)
alllights.addGroup(lightGr13)
alllights.addGroup(lightGr14)
alllights.addGroup(lightGr15)
alllights.addGroup(lightGr16)


InitModule(__name__)
