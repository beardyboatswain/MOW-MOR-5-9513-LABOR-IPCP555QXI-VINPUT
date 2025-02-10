#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from extronlib import event, Version
from extronlib.ui import Label

from lib.utils.system_init import InitModule

from lib.gui.SplashScreen import SplashScreen

from usr.dev.dev import ipads, ipad_usr, ipad_adm

from usr.var.system_room_vars import ROOM_NAME_USR, ROOM_NAME_ADM

import lib.utils.display_datatime as display_datatime

from lib.utils.debugger import debuggerNet as debugger
from usr.var.debug_mode import common_dbg
dbg = debugger(common_dbg, __name__)


# --- splash screens ------------------------------------------------------------------------------
splash_adm = SplashScreen(uiHost=ipad_adm, ppPageName="998_Splash_MP", lblNoteId=10004, btnSpinerId=10005)
splash_usr = SplashScreen(uiHost=ipad_usr, ppPageName="998_Splash_MP", lblNoteId=10004, btnSpinerId=10005)

# --- room name -----------------------------------------------------------------------------------
lblRoomNameID = 10001
lblRoomNames = []

# instancing labels for room names for all gui
for ipad in ipads:
    lblRoomName = Label(ipad, lblRoomNameID)
    if (ipad == ipad_usr):
        lblRoomName.SetText(ROOM_NAME_USR)
    elif (ipad == ipad_adm):
        lblRoomName.SetText(ROOM_NAME_ADM)
    lblRoomNames.append(lblRoomName)


InitModule(__name__)
