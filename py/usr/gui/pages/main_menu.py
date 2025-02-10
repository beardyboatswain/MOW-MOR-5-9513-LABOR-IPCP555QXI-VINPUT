#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.utils.system_init import InitModule

from usr.dev.dev import ipad_adm
from lib.gui.menu.CMenu import CMenuSignal


mainMenu = CMenuSignal(ipad_adm, 9, '020_MainMenu_PP')

mainMenu.addMenuButton(11,
                       'Home\n ',
                       'Home',
                       '100_Home_P',
                       homeP=True)

mainMenu.addMenuButton(21,
                       'Video\n ',
                       'Video - Main',
                       '200_Video_Main_P',
                       submenuName='022_MainMenu_SubVideo_PP',
                       closeSubmenuButtonID=20)
mainMenu.addMenuButton(22,
                       'Main\n',
                       'Video - Main',
                       '200_Video_Main_P',
                       parentButtonID=21)
mainMenu.addMenuButton(23,
                       'All\nConnections',
                       'Video - All Connections',
                       '210_Video_All_P',
                       parentButtonID=21)
mainMenu.addMenuButton(24,
                       'Linked\n ',
                       'Video - Linked',
                       '220_Video_Linked_P',
                       parentButtonID=21)
mainMenu.addMenuButton(25,
                       'Virtual\nSources',
                       'Video - Virtual Sources',
                       '230_Video_Virtual_P',
                       parentButtonID=21)
mainMenu.addMenuButton(26,
                       'Layouts\n',
                       'Video - Layouts',
                       '240_Video_VideoWall_P',
                       parentButtonID=21)

mainMenu.addMenuButton(31,
                       'Audio\n ',
                       'Audio - Main',
                       '300_Audio_Main_P',
                       submenuName='023_MainMenu_SubAudio_PP',
                       closeSubmenuButtonID=30)
mainMenu.addMenuButton(32,
                       'Main\n ',
                       'Audio - Main',
                       '300_Audio_Main_P',
                       parentButtonID=31)
mainMenu.addMenuButton(33,
                       'Mics\n ',
                       'Audio - Mics',
                       '301_Audio_Mics_P',
                       parentButtonID=31)
mainMenu.addMenuButton(34,
                       'Ties\n ',
                       'Audio - Ties',
                       '302_Audio_Ties_P',
                       parentButtonID=31)
mainMenu.addMenuButton(35,
                       'Input\nLevels',
                       'Audio - Input Levels',
                       '303_Audio_InputGains_P',
                       parentButtonID=31)
mainMenu.addMenuButton(36,
                       'Output\nLevels',
                       'Audio - Output Levels',
                       '304_Audio_OutputGains_P',
                       parentButtonID=31)

mainMenu.addMenuButton(41,
                       'Cams\n ',
                       'Cams - Control',
                       '400_Cams_Control_P',
                       submenuName='024_MainMenu_SubCams_PP',
                       closeSubmenuButtonID=40)
mainMenu.addMenuButton(42,
                       'Control\n ',
                       'Cams - Control',
                       '400_Cams_Control_P',
                       parentButtonID=41)
mainMenu.addMenuButton(43,
                       'Zones\n ',
                       'Cams - Zones',
                       '401_Cams_Zones_P',
                       parentButtonID=41)
mainMenu.addMenuButton(44,
                       'Tracking\n ',
                       'Cams - Tracking',
                       '402_Cams_Tracking_P',
                       parentButtonID=41)

mainMenu.addMenuButton(51,
                       'Operator\n ',
                       'Operator - VCS',
                       '500_Oper_VCS_P',
                       submenuName='025_MainMenu_SubOper_PP',
                       closeSubmenuButtonID=50)
mainMenu.addMenuButton(52,
                       'VCS\n ',
                       'Operator - VCS',
                       '500_Oper_VCS_P',
                       parentButtonID=51)
mainMenu.addMenuButton(53,
                       'Video-\nsupport',
                       'Operator - Videosupport',
                       '501_Oper_VideoSupport_P',
                       parentButtonID=51)

mainMenu.addMenuButton(61,
                       'Power\n ',
                       'Power - Devices',
                       '600_Power_Devices_P',
                       submenuName='026_MainMenu_SubPower_PP',
                       closeSubmenuButtonID=60)
mainMenu.addMenuButton(62,
                       'Devices\n ',
                       'Power - Devices',
                       '600_Power_Devices_P',
                       parentButtonID=61)
mainMenu.addMenuButton(63,
                       'Lights\n ',
                       'Power - Lights',
                       '601_Power_Lights_P',
                       parentButtonID=61)
mainMenu.addMenuButton(64,
                       'PDUs\n ',
                       'Power - PDUs',
                       '601_Power_Lights_P',
                       parentButtonID=61)

mainMenu.addMenuButton(71,
                       'Options\n ',
                       'Options - Common',
                       '900_Settings_Basic_P',
                       submenuName='029_MainMenu_SubOptions_PP',
                       closeSubmenuButtonID=70)
mainMenu.addMenuButton(72,
                       'Common\n ',
                       'Options - Common',
                       '900_Settings_Basic_P',
                       parentButtonID=71)
mainMenu.addMenuButton(73,
                       'Statuses\n ',
                       'Options - Statuses',
                       '901_Settings_Statuses_P',
                       parentButtonID=71)

mainMenu.showMenu()


InitModule(__name__)
