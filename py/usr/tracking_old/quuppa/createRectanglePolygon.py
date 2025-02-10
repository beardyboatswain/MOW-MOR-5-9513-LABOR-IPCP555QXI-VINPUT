#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# a - bottom left point of rectangle
# b - top right point of rectangle
a = ("12.17", "4.00")
b = ("16.18", "10.28")


f = a[0] + "," + a[1] + "|" + a[0] + "," + b[1] + "|" + b[0] + "," + b[1] + "|" + b[0] + "," + a[1] + "|" + a[0] + "," + a[1]
print(f)
