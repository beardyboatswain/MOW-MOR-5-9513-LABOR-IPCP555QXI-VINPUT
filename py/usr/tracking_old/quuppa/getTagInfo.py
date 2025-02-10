#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import urllib.error
import urllib.request

from extronlib.system import Timer

quuppa_ip = "10.213.142.57"
quuppa_port = 8080

resp = urllib.request.urlopen("http://{}:{}/qpe/getTagInfo?version=2".format(quuppa_ip, quuppa_port))

quuppaAnswer = resp.read()
quuppaTags = json.loads(quuppaAnswer.decode("utf-8"))

jsonFile = open(".\\py\\quuppa\\getTagInfo.json", "w")
jsonFile.write(json.dumps(quuppaTags, indent=2))
jsonFile.close()

sTags = ""

for tagI in quuppaTags["tags"]:
    tagName = tagI["name"]
    tagID = tagI["id"]

    sTags += tagID + "\t" + tagName + "\n"

tagFile = open(".\\py\\quuppa\\getTagInfo.tags", "w")
tagFile.write(sTags)
tagFile.close()
