#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.utils.system_init import InitModule
from lib.gui.PanelLocker import PanelLocker

from usr.dev.dev import ipad_usr, ipad_adm

from usr.gui.pages.pages_popups import usr_locker_mp_name

usr_gui_locker = PanelLocker(uiHost=ipad_usr, ppPageName=usr_locker_mp_name)
usr_gui_locker.addLockBtn(uiHost=ipad_adm, btnLockTglId=10006)

InitModule(__name__)
