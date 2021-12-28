#!/bin/python3

"""
calendar.d/html-try.py

Author: Edward Birdsall

Function: This file sets up needed variables for a calendar HTML display
          The calendar here is just for display.  Adding appointments and changing views is done by menu selections
Calls: mcalendar.jhtml

Variables:
     hd:   Web/TC/Tk page
     hdr: dictionary with calendar header infomration
          name - name of calendar
          page - month year Calendar
          today - day of week and date of current day
     days:days of week
     colorsm - dictionary with colors for background of dates
          priormonth, thisbefore, today, thismonth, nextmonth, site, neutral, calSclr
     tdy - dictionary array of information for the days to be displayed
          bgtclr - background today clear
          bgeclr - background event clear
          dnum - day number
          devt - number of day's events
          devt1t - day event today first title
          devt1c - day event today first calendar color
          devt2t - day event today second title
          devt2c - day event today second calendar color
          devt3t - day event today third title
          devt3c - day event today third calendar color
          devt4t - day event today fourth title
          devt4c - day event today fourth calendar color
     cal - calendar display and control information
          month - Display Month
          year - Display Year
          startwk - week number for first display week
          calrows - number of rows of calendar to be displayed
          calAt - name of first calendar
          calBt - name of second calendar
          calCt - name of third calendar
          calDt - name of fourth calendar
          calEt - name of fifth calendar
     pref - dictionary of user preferences
          startday - the starting day of the week 1=Monday, 0 or 7 is Sunday
          calAclr - color for first calendar
          calBclr - color for second calendar
          calCclr - color for third calendar
          calDclr - color for fourth calendar
          calEclr - color for fifth calendar
     dts = list of day numbers used to set up tdy[x]["dnum"]


"""

from jinja2 import Environment, FileSystemLoader

hd = {"loc":"Month Calendar"}
hdr = { "name":"Ed",  "page":"March 2019 Calendar", "today":"Saturday  March  2, 2019" }

days = ('Sunday Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split())
colorsm = {"priormonth": "Orchid", "thisbefore": "Aqua",  "today": "Yellow",  "thismonth": "White",  "nextmonth": "Lime", "site":"Red" , "neutral": "silver", "calSclr": "red" }

# devt is intended to hold the number of events for the day to be used in the template with an if or for but can't get to work right now
tdy = []
for i in range(0, 35,1):
     tdy.append({"bgtclr":"white","bgeclr":"white", "dnum":0, "devt":-1, "devt1t":"", "devt1c":"",  "devt2t":"", "devt2c":"",  "devt3t":"", "devt3c":"",  "devt4t":"", "devt4c":"", })
 

cal = {"month":"March", "year":"2019", "startwk":8,"calrows":5, "calAt":"Liturgical", "calBt":"US Holidays","calCt":"Birdsall Family", "calDt":"Kirkup Family", "calEt":""}
pref = {  "startDay":1,  "calAclr": "yellowgreen",  "calBclr": "lightsteelblue",  "calCclr": "cyan",  "calDclr": "magenta",  "calEclr": "purple"}
dts = [25, 26, 27, 28, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7  ]

for i in range(0, 4):
          tdy[i]["bgtclr"] = colorsm["priormonth"]
          tdy[i]["bgeclr"] = colorsm["priormonth"]

for i in range(35, 42):
          tdy[i]["bgtclr"] = colorsm["nextmonth"]
          tdy[i]["bgeclr"] = colorsm["nextmonth"]

for i in range(0,42,1):
     tdy[i]["dnum"] = dts[i]


tdy[4]["bgtclr"] = colorsm["thisbefore"]
tdy[4]["beeclr"] = colorsm["thisbefore"]
tdy[5]["bgtclr"] = colorsm["today"]
tdy[5]["beeclr"] = colorsm["today"]

tdy[4]["devt"] = 1
tdy[4]["dev1t"] =  "Bryan Kovas B'day"
tdy[4]["dev1c"] =pref["calCclr"]
tdy[6]["devt"] = 1
tdy[6]["dev1t"] =  "Helen Birdsall B'day"
tdy[6]["dev1c"] =pref["calCclr"]
tdy[6]["devt"] = 3
tdy[6]["dev1t"] =  "Greg Kovas B'day"
tdy[6]["dev1c"] =pref["calCclr"]
tdy[6]["dev2t"] =  "Brielle Balmer B'day"
tdy[6]["dev2c"] =pref["calCclr"]
tdy[6]["dev3t"] =  "Andrew Noyes B'day"
tdy[6]["dev3c"] =pref["calCclr"]

tdy[9]["devt"] = 1
tdy[9]["dev1t"] =  "Ash Wednesday"
tdy[9]["dev1c"] =pref["calAclr"]
tdy[13]["devt"] = 1
tdy[13]["dev1t"] =  "DST begins"
tdy[13]["dev1c"] = pref["calBclr"]
tdy[21]["devt"] = 1


input_ = {"hd":hd, "hdr":hdr, "cal":cal, "days":days, "colorsm":colorsm, "pref":pref, "tdy":tdy }
env = Environment(loader = FileSystemLoader("../templates/"))
template=env.get_template("mcalendar.jhtml")

output = template.render(input_ )

print(output)

