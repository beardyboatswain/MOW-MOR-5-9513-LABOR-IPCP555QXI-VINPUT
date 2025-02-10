#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.utils.system_init import InitModule
from lib.power.powerControl import SystemPower

from usr.dev.dev import ipad_adm, ipad_usr
from usr.gui.common import splash_usr


room_sys_power = SystemPower(pName="System Power")

room_sys_power.setMechanics(uiHost=ipad_usr,
                            btnTglID=901,
                            lblSateID=902,
                            lblNameID=903)

room_sys_power.setMechanics(uiHost=ipad_adm,
                            btnTglID=901,
                            lblSateID=902,
                            lblNameID=903)

room_sys_power.addSplashScreen(splash_usr)
room_sys_power.addPageTpansitions(ipad_usr, powerOnPage="100_Home_P", powerOffPage="000_Start_P")

InitModule(__name__)
