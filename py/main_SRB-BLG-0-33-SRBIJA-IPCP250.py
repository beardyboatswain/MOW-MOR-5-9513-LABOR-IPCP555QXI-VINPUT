#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.utils.system_init import InitMain

from usr.dev.dev import mIPCP, ipad_adm

import usr.gui.common
import usr.gui.datetime
import usr.gui.pages.pages_popups
import usr.gui.pages.main_menu
import usr.power.pdu_control
import usr.power.system_power
import usr.gui.pages.user_locker
import usr.gui.room_operation_mode
import usr.lcds.lcd_control

import usr.cams.cam_control
import usr.video.video_control
# import usr.audio.audio_control


import usr.trackingV2.tracking_system

# import usr.dev.servers.autotrackServer


# import usr.trackingV2.tracking
# import usr.dev.dev_cameras
# import usr.gui.cams.gui_cam_control



# import usr.gui.power.gui_lcd_power

# import usr.gui.power.gui_stage_lights


InitMain(__name__)
