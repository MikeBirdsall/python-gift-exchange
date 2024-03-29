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
import calendar
import datetime

#=========================================================================================================
#Begining of definitions.  Need to remember how to split this into a seperate area that invokes MCalendar
#=========================================================================================================
#=================================
# desired inputs for final version what, when, which event calendars, preferences
#=================================
inputs = {"name":"Ed", "date":"March 2, 2019", "startDay":6,}
#========================================================
# some kludges for testing and until I get it all working
#========================================================
#cyear = int(cal.get("year"))
cyear = 2019
cmonth = 3
cday = 2
cals= [
      dict(num=0, app="FALSE", name="Liturgical", color="yellowgreen"),
      dict(num=1, app="FALSE", name="US Holidays", color="lightsteelblue"),
      dict(num=2, app="TRUE", name="Birdsall Family", color="cyan"),
      dict(num=3, app="TRUE", name="Kirkup Family",color="magenta"),
      dict(num=4, app="FALSE", name="", color="purple"),
      dict(num=5, app="TRUE", name="Site", color="red")
]
eventCal = [
           dict(num=0, cal="Liturgical", eDate=datetime.date(2019, 2, 24), title="Ordinary 8th Sunday"),
           dict(num=1, cal="Liturgical", eDate=datetime.date(2019, 3, 3), title="Ordinary 9th Sunday"),
           dict(num=2, cal="Liturgical", eDate=datetime.date(2019, 3, 6), title="Ash Wednesday"),
           dict(num=3, cal="US Holidays", eDate=datetime.date(2019, 3, 9), title="DST begins"),
           dict(num=4, cal="Liturgical", eDate=datetime.date(2019, 3, 10), title="Lent 1st Sunday"),
           dict(num=5, cal="Liturgical", eDate=datetime.date(2019, 3, 17), title="Lent 2nd Sunday"),
           dict(num=6, cal="Liturgical", eDate=datetime.date(2019, 3, 24), title="Lent 3rd Sunday"),
           dict(num=7, cal="Liturgical", eDate=datetime.date(2019, 3, 31), title="Lent 4th Sunday"),
           dict(num=8, cal="Birdsall Family", eDate=datetime.date(2019, 3, 1), title="Bryan Kovas B'Day" ),
           dict(num=9, cal="Birdsall Family", eDate=datetime.date(2019, 3, 3), title="Helen Birdsall B'Day"),
           dict(num=10, cal="Birdsall Family", eDate=datetime.date(2019, 3, 4), title="Greg Kovas B'Day"),
           dict(num=11, cal="Birdsall Family", eDate=datetime.date(2019, 3, 4), title="Andrew Noyes B'Day"),
           dict(num=12, cal="Birdsall Family", eDate=datetime.date(2019, 3, 4), title="Brielle Balmer B'Day"),
]

#===================================
# Working code towards final version
#===================================

hd = {"loc":"Month Calendar"}
hdr = { "name":"Ed",  "page":"March 2019 Calendar", "today":"Saturday  March  2, 2019" }
hdr["name"] = inputs["name"]
hdr["page"] = datetime.datetime.strptime(inputs["date"], "%B %d, %Y").strftime("%B %Y")+" Calendar"
#hdr["today"] = datetime.datetime.now().strftime("%A %B %d, %Y")
hdr["today"] = "Saturday March 02, 2019"  #for testing

cal = {"month":"March", "year":"2019", "startwk":5,"calrows":5, "calAt":"Liturgical", "calBt":"US Holidays","calCt":"Birdsall Family", "calDt":"Kirkup Family", "calEt":""}
pref = {  "startDay":1,  "calAclr": "yellowgreen",  "calBclr": "lightsteelblue",  "calCclr": "cyan",  "calDclr": "magenta",  "calEclr": "purple"}
pref["startDay"] = inputs["startDay"]

if (inputs["startDay"] == 6):  # Week starts on Sunday
     cal["startwk"] = int(datetime.date(cyear, cmonth, cday).strftime("%U"))
else:                        #Week starts on Monday
     cal["startwk"] = int(datetime.date(cyear, cmonth, cday).strftime("%W"))

glcal = calendar.Calendar(inputs["startDay"])
days = [calendar.day_name[i] for i in glcal.iterweekdays()]
dts = []
dmt = []
for i in glcal.itermonthdates(cyear, cmonth):
     dts.append( i.day )
     dmt.append( i.month )

numdays = len(dts)
cal["calrows"] = numdays//7

#days = ('Sunday Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split())
colorsm = {"priormonth": "Orchid", "thisbefore": "Aqua",  "today": "Yellow",  "thismonth": "White",  "nextmonth": "Lime", "site":"Red" , "neutral": "silver", "calSclr": "red" }

tdy = []
for i in range(0, 42,1):
     tdy.append({"bgtclr":"white","bgeclr":"white", "mnum":0, "dnum":0, "devt":-1, "dev1t":"", "dev1c":"gray85", "dev1e":"",  "dev2t":"", "dev2c":"gray85", "dev2e":"", "dev3t":"", "dev3c":"gray85", "dev3e":"", "dev4t":"", "dev4c":"grey85", "dev4e":"", })
 
for i in range(0, numdays, 1):
     tdy[i]["mnum"] = dmt[i]
     tdy[i]["dnum"] = dts[i]
     if (dmt[i] < cmonth):
          tdy[i]["bgtclr"] = colorsm["priormonth"]
          tdy[i]["bgeclr"] = colorsm["priormonth"]
     elif (dmt[i] > cmonth ):
          tdy[i]["bgtclr"] = colorsm["nextmonth"]
          tdy[i]["bgeclr"] = colorsm["nextmonth"]
     else:
          if (dts[i] < cday):
               tdy[i]["bgtclr"] = colorsm["thisbefore"]
               tdy[i]["beeclr"] = colorsm["thisbefore"]
          elif (dts[i] == cday):
               tdy[i]["bgtclr"] = colorsm["today"]
               tdy[i]["beeclr"] = colorsm["today"]
          else:
               tdy[i]["bgtclr"] = colorsm["thismonth"]
               tdy[i]["beeclr"] = colorsm["thismonth"]

for i in range(0, 42, 1):
     for ii in range(0,len(eventCal),1):
          if ((tdy[i]["mnum"] == eventCal[ii]["eDate"].month) and (tdy[i]["dnum"] == eventCal[ii]["eDate"].day)):
               if (tdy[i]["devt"]<1):
                    tdy[i]["devt"] = 1
               else:
                    tdy[i]["devt"] = tdy[i]["devt"] + 1
               if (tdy[i]["devt"] == 1):
                    tdy[i]["dev1t"] = eventCal[ii]["title"]
                    for iii in range(0,len(cals),1):
                         if (cals[iii]["name"] == eventCal[ii]["cal"]):
                              tdy[i]["dev1c"] = cals[iii]["color"]
                              if (cals[iii]["app"] == "TRUE"):
                                   tdy[i]["dev1e"] = "Show "+ eventCal[ii]["title"]
               elif (tdy[i]["devt"] == 2):
                    tdy[i]["dev2t"] = eventCal[ii]["title"]
                    for iii in range(0,len(cals),1):
                         if (cals[iii]["name"] == eventCal[ii]["cal"]):
                              tdy[i]["dev2c"] = cals[iii]["color"]
                              if (cals[iii]["app"] == "TRUE"):
                                   tdy[i]["dev2e"] = "Show "+ eventCal[ii]["title"]
               elif (tdy[i]["devt"] == 3):
                    tdy[i]["dev3t"] = eventCal[ii]["title"]
                    for iii in range(0,len(cals),1):
                         if (cals[iii]["name"] == eventCal[ii]["cal"]):
                              tdy[i]["dev3c"] = cals[iii]["color"]
                              if (cals[iii]["app"] == "TRUE"):
                                   tdy[i]["dev3e"] = "Show "+ eventCal[ii]["title"]
               elif (tdy[i]["devt"] == 4):
                    tdy[i]["dev4t"] = eventCal[ii]["title"]
                    for iii in range(0,len(cals),1):
                         if (cals[iii]["name"] == eventCal[ii]["cal"]):
                              tdy[i]["dev4c"] = cals[iii]["color"]
                              if (cals[iii]["app"] == "TRUE"):
                                   tdy[i]["dev4e"] = "Show "+ eventCal[ii]["title"]
               else:
                    tdy[i]["devt"] = 4



input_ = {"hd":hd, "hdr":hdr, "cal":cal, "days":days, "colorsm":colorsm, "pref":pref, "tdy":tdy }
env = Environment(loader = FileSystemLoader("../templates/"))
template=env.get_template("mcalendar.jhtml")

output = template.render(input_ )

print(output)

