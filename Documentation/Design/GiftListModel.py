#!/bin/python3

"""
calendar display prep

Author: Edward Birdsall

Function: This function sets up needed variables for a calendar display
          The calendar here is just for display.  Adding events and changing views is done by menu selections
Calls: mcalendar.jhtml or mcalendar.py

Variables:
     hd:   Web-TCL/Tk page
     hdr: dictionary with calendar header information
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

"""
These lines are for display
     hd = {"loc":"Month Calendar"}
     hdr = { "name":"Ed",  "page":"March 2019 Calendar", "today":"Saturday  March  2, 2019" }
     cal = {"month":"March", "year":"2019", "startwk":8,"calrows":5, "calAt":"Liturgical", \
            "calBt":"US Holidays","calCt":"Birdsall Family", "calDt":"Kirkup Family", "calEt":""}
     pref = {"startDay":1,  "calAclr": "yellowgreen",  "calBclr": "lightsteelblue", \
             "calCclr": "cyan",  "calDclr": "magenta",  "calEclr": "purple"}

"""

class WLCalendar(Calendar)
"""
Calendar methods and objects for the WishList application.     
"""     


     def __init__(self):
          super().__init__()

          self.initCal()

     def initCal(self):
     
     def PrepareBareCalendarDisplay(month, year, day, weekstart):
     """
     This prepares the variables for use in either the HTML or Tkinter displays
     This uses the Gregorian Calendar and is meant for current years
     Input to this is the month&year or month, day and year for the calendar along with the 
          starting day of week
     Output is set up for a 4,5, or 6 weeks display of the desired month, filled out as necessary
          for even week
     """
     
     
     
     days = ('Sunday Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split())
     colorsm = {"priormonth": "Orchid", "thisbefore": "Aqua",  "today": "Yellow", \
                "thismonth": "White",  "nextmonth": "Lime", "site":"Red" , "neutral": "silver", \
                "calSclr": "red" }
     a_cal = calendar. (month, year)
     priorMonth =
     nextMonth =
     initial_yearDayNumber = 
     cal["month"] = month
     cal["year"] = year
     cal["startwk"] = a_cal.wknum
     cal["calrows"] = len(a_cal)/7
     pref["startDay"] = weekstart
     tdy = []
     for i in range(0, len(a_cal),1):
          tdy.append({"yearDayNumber":"1", "bgtclr":"white","bgeclr":"white", "dnum":0, "devt":0,\
                      "devt1t":"", "devt1c":"",  "devt2t":"", "devt2c":"",  "devt3t":"", \
                      "devt3c":"", "devt4t":"", "devt4c":"", })
     
     for i in range(0,len(a_cal),1):
          tdy[i]["yearDayNumber"] = initial_yearDayNumber + i
          tdy[i]["dnum"] = a_cal[i][day]
          case a_cal[i]["month]
               priorMonth)
                    tdy[i]["bgtclr"] = colorsm["priormonth"]
                    tdy[i]["bgeclr"] = colorsm["priormonth"]
               thisMonth)
                    tdy[i]["bgtclr"] = colorsm["thisbefore"]
                    tdy[i]["beeclr"] = colorsm["thisbefore"]
                    today
                    tdy[i]["bgtclr"] = colorsm["today"]
                    tdy[i]["beeclr"] = colorsm["today"]
                    after today
                    tdy[i]["bgtclr"] = colorsm["thisafter"]
                    tdy[i]["beeclr"] = colorsm["thisafter"]
               nextMonth)
                    tdy[i]["bgtclr"] = colorsm["nextmonth"]
                    tdy[i]["bgeclr"] = colorsm["nextmonth"]
          esac

     pass

     def AddCalendarToDisplay(myCalendar, tdy)
     """
     This adds calendar events to a Calendar Display
     Input is name and color of Calendar, the calendar and date range to be displayed.
     """
     
     for i in range():
          # locate any event on tdy[i]["yearDayNumber"]
          # for each event on that day then increment tdy[i]["devt"] and add dev_t = title dev_c=color
     

     pass
     
     def AddEvent()
     """
     This method adds an event to a calendar specified by one of the Administrators.
     For the Wish List events are all day events like birthdays or holidays.
     """
     pass
     
class WLPerson()
"""
This class 
"""
     def AddPerson();
     """
     This method is to initialize a person and set in initial values.
     """
     pass
     
     def UpdatePassword();
     """
     This method is to allow a person to update their password in use.
     """
     pass
     
     def ModifyPerson();
     """
     This method is to allow an Administrator to change information on a person that the user can not change.
     These things include name, clan, birthday.
     """
     pass
     
     def EditPerson();
     """
     This method allows a user to change some of their personal information
     """
     pass

     def ArchivePerson();
     """
     This method marks a person as inactive.
     """
     pass

     def AddClan(clanName, clanDescription, clanAdministrator);
     """
     This method initializes a clan with a name and administrator.
     """
     pass

     def EditClan();
     """
     This method is to modify the clan membership by the clan administrator
     """
     pass

     def ArchiveClan();
     """
     This method marks a clan as inactive.
     """
     pass

class WLWish
"""
"""

     def AddWish();
     """
     This method is to add a new wish to a person's wish list suggested by them or for them.
     """
     pass

     def ModifyWish();
     """
     This method allows a user to modify their wish.
     """
     pass

     def EditWish();
     """
     """
     pass

     def PurgeWish();
     """
     """
     pass

     def AddGift();
     """
     """
     pass

     def EditGift();
     """
     """
     pass

     def ArchiveGift();
     pass

