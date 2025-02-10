#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.utils.system_init import InitModule

import lib.utils.display_datatime as display_datatime
from usr.dev.dev import ipad_adm


dabeLabelID = 10002
timeLabelID = 10003

datetime_widgets = [display_datatime.ShowDateTime(UIDev=ipad_adm,
                                                  dateLabelID=dabeLabelID,
                                                  timeLabelID=timeLabelID,
                                                  lang="en"),]


InitModule(__name__)
