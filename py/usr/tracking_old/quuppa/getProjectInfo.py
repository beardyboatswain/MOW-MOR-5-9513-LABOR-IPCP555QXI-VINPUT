#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import urllib.error
import urllib.request

import re

from extronlib.system import Timer

quuppa_ip = "10.213.142.57"
quuppa_port = 8080

resp = urllib.request.urlopen("http://{}:{}/qpe/getProjectInfo?version=2&noImageBytes=true".format(quuppa_ip, quuppa_port))

quuppaAnswer = resp.read()
quuppaInfo = json.loads(quuppaAnswer.decode("utf-8"))

jsonFile = open(".\\py\\quuppa\\getProjectInfo.json", "w")
jsonFile.write(json.dumps(quuppaInfo, indent=2))
jsonFile.close()


zoneFile = open(".\\py\\quuppa\\getProjectInfo_Zones.json", "w")
coordinateSystems = quuppaInfo.get("coordinateSystems")

coordsPattern = "(\d{1,2}.\d{2}),(\d{1,2}.\d{2})"
coordsMatchPattern = re.compile(coordsPattern)

tZones = {}

for item in coordinateSystems:
    for zone in item.get("zones"):
        coordsMatchObjects = coordsMatchPattern.findall(zone.get("polygonData"))
        if (coordsMatchObjects and len(coordsMatchObjects) == 5):
            cornerLeftBottom = (int(float(coordsMatchObjects[0][0])) * 1000, int(float(coordsMatchObjects[0][1]) * 1000))
            cornerRightTop = (int(float(coordsMatchObjects[2][0])) * 1000, int(float(coordsMatchObjects[2][1]) * 1000))
        tZones[zone.get("id")] = {"name": zone.get("name"),
                                  "polygonData": zone.get("polygonData"),
                                  "p1": cornerLeftBottom,
                                  "p2": cornerRightTop
                                  }
json.dump(tZones, zoneFile, indent=2)
zoneFile.close()
