#!/bin/python3

from jinja2 import Environment, FileSystemLoader

hd = {"loc":"Month Calendar"}
hdr = { "name":"Ed",  "page":"March 2019 Calendar", "today":"Saturday  March  2, 2019" }

days = ('Sunday Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split())
colorsm = {"priormonth": "DarkOrchid", "thisbefore": "Aqua",  "today": "Yellow",  "thismonth": "White",  "nextmonth": "Lime", "site":"Red" , "neutral": "silver", "calSclr": "red" }

# devt is intended to hold the number of events for the day to be used in the template with an if or for but can't get to work right now
tdy = []
for i in range(0, 35,1):
     tdy.append({"bgtclr":"white","bgeclr":"white", "dnum":0, "devt":-1, "devt1t":"", "devt1c":"",  "devt2t":"", "devt2c":"",  "devt3t":"", "devt3c":"",  "devt4t":"", "devt4c":"", })
 

cal = {"month":"March", "year":"2019", "startwk":5, "calAt":"Liturgical", "calBt":"US Holidays","calCt":"Birdsall Family", "calDt":"Kirkup Family", "calEt":""}
pref = {  "startDay":1,  "calAclr": "green",  "calBclr": "blue",  "calCclr": "cyan",  "calDclr": "magenta",  "calEclr": "purple"}
dts = [25, 26, 27, 28, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31 ]

for i in range(0, 4):
          tdy[i]["bgtclr"] = colorsm["priormonth"]
          tdy[i]["bgeclr"] = colorsm["priormonth"]


for i in range(0,35,1):
     tdy[i]["dnum"] = dts[i]


tdy[4]["bgtclr"] = colorsm["thisbefore"]
tdy[4]["beeclr"] = colorsm["thisbefore"]
tdy[5]["bgtclr"] = colorsm["today"]
tdy[5]["beeclr"] = colorsm["today"]
tdy[9]["devt"] = 1
tdy[9]["dev1t"] =  "Ash Wednesday"
tdy[9]["dev1c"] =pref["calAclr"]
tdy[13]["devt"] = 1
tdy[13]["dev1t"] =  "DST begins"
tdy[13]["dev1c"] = pref["calBclr"]
tdy[21]["devt"] = 1
tdy[21]["dev1t"] =  "President's Day"
tdy[21]["dev1c"] = pref["calBclr"]


input_ = {"hd":hd, "hdr":hdr, "cal":cal, "days":days, "colorsm":colorsm, "pref":pref, "tdy":tdy }
env = Environment(loader = FileSystemLoader("."))
template=env.get_template("calendar3.html")

output = template.render(input_ )

print(output)

