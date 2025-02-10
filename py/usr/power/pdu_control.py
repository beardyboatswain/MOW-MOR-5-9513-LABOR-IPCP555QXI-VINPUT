#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.utils.system_init import InitModule
from lib.power.AtenPDU import AtenPDUTelnet

from usr.dev.dev import ipad_adm
from usr.dev.dev import (aten_pdu_1_connection,
                         aten_pdu_2_connection,
                         aten_pdu_3_connection,
                         aten_pdu_4_connection,
                         aten_pdu_5_connection,
                         aten_pdu_6_connection)


aten_pdu_1 = AtenPDUTelnet(device=aten_pdu_1_connection, outletSize=8)
aten_pdu_2 = AtenPDUTelnet(device=aten_pdu_2_connection, outletSize=8)
aten_pdu_3 = AtenPDUTelnet(device=aten_pdu_3_connection, outletSize=8)
aten_pdu_4 = AtenPDUTelnet(device=aten_pdu_4_connection, outletSize=8)
aten_pdu_5 = AtenPDUTelnet(device=aten_pdu_5_connection, outletSize=8)
aten_pdu_6 = AtenPDUTelnet(device=aten_pdu_6_connection, outletSize=8)

# aten_pdu_1.add_tgl_all_btn(ipad_adm, 7101)
# aten_pdu_2.add_tgl_all_btn(ipad_adm, 7102)
# aten_pdu_3.add_tgl_all_btn(ipad_adm, 7103)
# aten_pdu_4.add_tgl_all_btn(ipad_adm, 7104)
# aten_pdu_5.add_tgl_all_btn(ipad_adm, 7105)
# aten_pdu_6.add_tgl_all_btn(ipad_adm, 7106)

aten_pdu_1.add_tgl_btn(ipad_adm, 7111, 1)
aten_pdu_1.add_tgl_btn(ipad_adm, 7112, 2)
aten_pdu_1.add_tgl_btn(ipad_adm, 7113, 3)
aten_pdu_1.add_tgl_btn(ipad_adm, 7114, 4)
aten_pdu_1.add_tgl_btn(ipad_adm, 7115, 5)
aten_pdu_1.add_tgl_btn(ipad_adm, 7116, 6)
aten_pdu_1.add_tgl_btn(ipad_adm, 7117, 7)
aten_pdu_1.add_tgl_btn(ipad_adm, 7118, 8)

aten_pdu_2.add_tgl_btn(ipad_adm, 7121, 1)
aten_pdu_2.add_tgl_btn(ipad_adm, 7122, 2)
aten_pdu_2.add_tgl_btn(ipad_adm, 7123, 3)
aten_pdu_2.add_tgl_btn(ipad_adm, 7124, 4)
aten_pdu_2.add_tgl_btn(ipad_adm, 7125, 5)
aten_pdu_2.add_tgl_btn(ipad_adm, 7126, 6)
aten_pdu_2.add_tgl_btn(ipad_adm, 7127, 7)
aten_pdu_2.add_tgl_btn(ipad_adm, 7128, 8)

aten_pdu_3.add_tgl_btn(ipad_adm, 7131, 1)
aten_pdu_3.add_tgl_btn(ipad_adm, 7132, 2)
aten_pdu_3.add_tgl_btn(ipad_adm, 7133, 3)
aten_pdu_3.add_tgl_btn(ipad_adm, 7134, 4)
aten_pdu_3.add_tgl_btn(ipad_adm, 7135, 5)
aten_pdu_3.add_tgl_btn(ipad_adm, 7136, 6)
aten_pdu_3.add_tgl_btn(ipad_adm, 7137, 7)
aten_pdu_3.add_tgl_btn(ipad_adm, 7138, 8)

aten_pdu_4.add_tgl_btn(ipad_adm, 7141, 1)
aten_pdu_4.add_tgl_btn(ipad_adm, 7142, 2)
aten_pdu_4.add_tgl_btn(ipad_adm, 7143, 3)
aten_pdu_4.add_tgl_btn(ipad_adm, 7144, 4)
aten_pdu_4.add_tgl_btn(ipad_adm, 7145, 5)
aten_pdu_4.add_tgl_btn(ipad_adm, 7146, 6)
aten_pdu_4.add_tgl_btn(ipad_adm, 7147, 7)
aten_pdu_4.add_tgl_btn(ipad_adm, 7148, 8)

aten_pdu_5.add_tgl_btn(ipad_adm, 7151, 1)
aten_pdu_5.add_tgl_btn(ipad_adm, 7152, 2)
aten_pdu_5.add_tgl_btn(ipad_adm, 7153, 3)
aten_pdu_5.add_tgl_btn(ipad_adm, 7154, 4)
aten_pdu_5.add_tgl_btn(ipad_adm, 7155, 5)
aten_pdu_5.add_tgl_btn(ipad_adm, 7156, 6)
aten_pdu_5.add_tgl_btn(ipad_adm, 7157, 7)
aten_pdu_5.add_tgl_btn(ipad_adm, 7158, 8)

aten_pdu_6.add_tgl_btn(ipad_adm, 7161, 1)
aten_pdu_6.add_tgl_btn(ipad_adm, 7162, 2)
aten_pdu_6.add_tgl_btn(ipad_adm, 7163, 3)
aten_pdu_6.add_tgl_btn(ipad_adm, 7164, 4)
aten_pdu_6.add_tgl_btn(ipad_adm, 7165, 5)
aten_pdu_6.add_tgl_btn(ipad_adm, 7166, 6)
aten_pdu_6.add_tgl_btn(ipad_adm, 7167, 7)
aten_pdu_6.add_tgl_btn(ipad_adm, 7168, 8)


aten_pdu_1.add_tgl_lbl(ipad_adm, 7211, 1, "Outlet 1")
aten_pdu_1.add_tgl_lbl(ipad_adm, 7212, 2, "Outlet 2")
aten_pdu_1.add_tgl_lbl(ipad_adm, 7213, 3, "Outlet 3")
aten_pdu_1.add_tgl_lbl(ipad_adm, 7214, 4, "Outlet 4")
aten_pdu_1.add_tgl_lbl(ipad_adm, 7215, 5, "Outlet 5")
aten_pdu_1.add_tgl_lbl(ipad_adm, 7216, 6, "Outlet 6")
aten_pdu_1.add_tgl_lbl(ipad_adm, 7217, 7, "Outlet 7")
aten_pdu_1.add_tgl_lbl(ipad_adm, 7218, 8, "Outlet 8")

aten_pdu_2.add_tgl_lbl(ipad_adm, 7221, 1, "Outlet 1")
aten_pdu_2.add_tgl_lbl(ipad_adm, 7222, 2, "Outlet 2")
aten_pdu_2.add_tgl_lbl(ipad_adm, 7223, 3, "Outlet 3")
aten_pdu_2.add_tgl_lbl(ipad_adm, 7224, 4, "Outlet 4")
aten_pdu_2.add_tgl_lbl(ipad_adm, 7225, 5, "Outlet 5")
aten_pdu_2.add_tgl_lbl(ipad_adm, 7226, 6, "Outlet 6")
aten_pdu_2.add_tgl_lbl(ipad_adm, 7227, 7, "Outlet 7")
aten_pdu_2.add_tgl_lbl(ipad_adm, 7228, 8, "Outlet 8")

aten_pdu_3.add_tgl_lbl(ipad_adm, 7231, 1, "Outlet 1")
aten_pdu_3.add_tgl_lbl(ipad_adm, 7232, 2, "Outlet 2")
aten_pdu_3.add_tgl_lbl(ipad_adm, 7233, 3, "Outlet 3")
aten_pdu_3.add_tgl_lbl(ipad_adm, 7234, 4, "Outlet 4")
aten_pdu_3.add_tgl_lbl(ipad_adm, 7235, 5, "Outlet 5")
aten_pdu_3.add_tgl_lbl(ipad_adm, 7236, 6, "Outlet 6")
aten_pdu_3.add_tgl_lbl(ipad_adm, 7237, 7, "Outlet 7")
aten_pdu_3.add_tgl_lbl(ipad_adm, 7238, 8, "Outlet 8")

aten_pdu_4.add_tgl_lbl(ipad_adm, 7241, 1, "Outlet 1")
aten_pdu_4.add_tgl_lbl(ipad_adm, 7242, 2, "Outlet 2")
aten_pdu_4.add_tgl_lbl(ipad_adm, 7243, 3, "Outlet 3")
aten_pdu_4.add_tgl_lbl(ipad_adm, 7244, 4, "Outlet 4")
aten_pdu_4.add_tgl_lbl(ipad_adm, 7245, 5, "Outlet 5")
aten_pdu_4.add_tgl_lbl(ipad_adm, 7246, 6, "Outlet 6")
aten_pdu_4.add_tgl_lbl(ipad_adm, 7247, 7, "Outlet 7")
aten_pdu_4.add_tgl_lbl(ipad_adm, 7248, 8, "Outlet 8")

aten_pdu_5.add_tgl_lbl(ipad_adm, 7251, 1, "Outlet 1")
aten_pdu_5.add_tgl_lbl(ipad_adm, 7252, 2, "Outlet 2")
aten_pdu_5.add_tgl_lbl(ipad_adm, 7253, 3, "Outlet 3")
aten_pdu_5.add_tgl_lbl(ipad_adm, 7254, 4, "Outlet 4")
aten_pdu_5.add_tgl_lbl(ipad_adm, 7255, 5, "Outlet 5")
aten_pdu_5.add_tgl_lbl(ipad_adm, 7256, 6, "Outlet 6")
aten_pdu_5.add_tgl_lbl(ipad_adm, 7257, 7, "Outlet 7")
aten_pdu_5.add_tgl_lbl(ipad_adm, 7258, 8, "Outlet 8")

aten_pdu_6.add_tgl_lbl(ipad_adm, 7261, 1, "Outlet 1")
aten_pdu_6.add_tgl_lbl(ipad_adm, 7262, 2, "Outlet 2")
aten_pdu_6.add_tgl_lbl(ipad_adm, 7263, 3, "Outlet 3")
aten_pdu_6.add_tgl_lbl(ipad_adm, 7264, 4, "Outlet 4")
aten_pdu_6.add_tgl_lbl(ipad_adm, 7265, 5, "Outlet 5")
aten_pdu_6.add_tgl_lbl(ipad_adm, 7266, 6, "Outlet 6")
aten_pdu_6.add_tgl_lbl(ipad_adm, 7267, 7, "Outlet 7")
aten_pdu_6.add_tgl_lbl(ipad_adm, 7268, 8, "Outlet 8")


InitModule(__name__)
