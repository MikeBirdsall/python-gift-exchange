#!/usr/bin/python3

"""
User Home Page using tkinter

Author: Edward Birdsall

Variables:
     hd:  Web/TCL/TK page
     hdr: dictionary with User Home Page header infomration
          name - name of calendar
          page - month year Calendar
          today - day of week and date of current day
     user:
     msgs:
     ss:
     evt:
     mod:
     wsh:
"""

from tkinter import *

class UHomePage(Frame):

     def __init__(self):
          super().__init__()

          self.initUI()

     def initUI(self):
          #========================================================================================
          #Begining of definitions.  Need to remember how to split this into a seperate area that
          # invokes MCalendar
          #========================================================================================
          hd = {"loc": "User Home"}
          hdr = dict(name="Ed", page="Home", today="Wednesday  March 06, 2019")
          user = {"firstn":"Edward", "lastn":"Birdsall", "bday":"23", "byr":"1952", "bmn":"April", 
               "pemail":"edwardbirdsall@elberton.net", "semail":"ntdgn@umich.edu", "clan":"Birdsall",
               "altwsh1":"http://Amazon_list_url", "proxy":"None" }
          msgs = {"new":0, "tot":10}
          ss = {"cyr":2018, "cypk":"Peggy Kovas" }
          evt = {"event1": "None", "bday1":"Mar 17 - Terri McIntosh", "bday2":"Mar 29 - Alexa Hodgins"}
          mod = {"who":"owner Edward Birdsall", "date":"Sunday Feb 24, 2019  13:15:12"}
          wsh = [
               dict(num=1, ndes="any", exp="never", des="Frangelico, B&B, Irish Mist"),
               dict(num=2, ndes="any", exp="never", des="Fudge - chocolate, peanut butter are favorites"),
               dict(num=3, ndes="any", exp="never", des="Wine - Favorites yellowtail-*, wallaby \
                    creek-*, and others"),
               dict(num=4, ndes="any", exp="never", des="Gift Certificate - Home Depot or Lowes"),
               dict(num=5, ndes="any", exp="never", des="Gift Certificate - Barnes and Noble"),
               dict(num=6, ndes="any", exp="never", des=("Gift Certificate - Right Stuf (www.rightstuf.com) Where I get most of my anime and shaw dvds")),
               dict(num=7, ndes="1",   des="Rasberry Pi Starter/learning kit", exp="Dec 26, 2019"),
               dict(num=8, ndes="any", exp="never", des=("Candle molds especially for the larger candles (larger than votive)")),
               dict(num=9, ndes="any", exp="Dec 26, 2019", des=("washable long ties for church (not dryclean) looking for ties with primary color rose, white.")),
               dict(num=10, ndes="1", exp="Dec 26, 2019", des="CD by The Fire - Inspired (found at store.cdbaby.com)"),
               dict(num=11, ndes="any", exp="Dec 26, 2020", des=("Short sleeve Shirts 16 neck in red, rose, green, violet - liturgical colors to wear to church (same as ties)")),
               dict(num=12, ndes="any", exp="Dec 26, 2020", des=("Washable Ties in red, rose, green, violet - liturgical colors to wear to church")),
               dict(num=13, ndes="1", exp="Sep 01, 2019", des="Wishlist in final test mode"),
               dict(num=14, ndes="1", des="2450 Canyon Sold", exp="Aug 1, 2019"),
               dict(num=15, ndes="1", exp="Dec 31, 2020", des="New House in 'Georgia"),
               ]

          #========================================================================================
          #Ending of definitions.  Need to remember how to split this into a seperate area that
          # invokes MCalendar
          #========================================================================================
          for i in range(0,30,1):
               self.rowconfigure(i, pad=3)
               
          for i in range(0,16,1):
               self.columnconfigure(1, minsize=15, pad=3)
               
          #Window Display
          self.master.title(hd.get("loc"))
          ht0 = Label(self,text=hdr.get("name")+"'s "+hdr.get("page"), justify=CENTER, relief="flat", 
                      background="lightblue", font=("Arial Bold", 20)).grid(row=0, rowspan=3, columnspan=16, \
                      sticky=W+E)
          ht2 = Label(self,text="Today's Date: "+hdr.get("today") , anchor=S, relief="flat", \
                      background="lightblue", font=("Arial Regular",10)).grid(row=3, columnspan=16, sticky=W+E) 
          #Header Display
          hdr_1 = Label(self, text="Information", justify=LEFT, font=("Times Bold", 10)).grid(row=4, column=0)
          hdr_2 = Label(self, text="Personal", anchor=E).grid(row=5, column=0, sticky=E)
          hdr_30 = Label(self, text="Full Name:", anchor=E).grid(row=6, column=1, sticky=E)
          hdr_31 = Label(self, text=user.get("firstn")+" "+user.get("lastn"), \
                        justify=RIGHT).grid(row=6, column=2, columnspan=2)
          hdr_31 = Label(self, text="Birthday: "+user.get("bmn")+" "+user.get("bday")+", "+user.get("byr"), \
                         justify=CENTER).grid(row=6, column=4)
          hdr_32 = Label(self, text="e-mail: "+user.get("pemail")+"   "+user.get("semail"), \
                         justify=CENTER).grid(row=6, column=5, columnspan=9)
          hdr_40 = Label(self, text="Clans:", font=("Times Bold",10)).grid(row=7, column=1)
          hdr_41 = Label(self, text=user.get("clan"), anchor=W).grid(row=7, column=2, columnspan=2, sticky=W)
          hdr_42 = Label(self, text="Messages: New:"+str(msgs.get("new"))+" Total: "+str(msgs.get("tot")),\
                         anchor=W).grid(row=7, column=4, columnspan=5, stick=W)
          hdr_5 = Label(self, text="Secret Santa").grid(row=8, column=0)
          hdr_6 = Label(self, text=user.get("clan")+": Secret Santa Christmas "+str(ss.get("cyr"))\
                        +": "+ss.get("cypk"), anchor=W).grid(row=9, column=1, columnspan=4, sticky=W)
          hdr_7 = Label(self, text="Upcoming Events:").grid(row=10, column=0)
          hdr_80 = Label(self, text=evt.get("event1")).grid(row=11, column=0)
          hdr_81 = Label(self, text="Birthdays: ").grid(row=11, column=1)
          hdr_82 = Label(self, text=evt.get("bday1")+"   "+evt.get("bday2"), anchor=W).grid(row=11, column=2, \
                         sticky=W, columnspan=4)
          
          #Buttons Row 1
          a_btn = Button(self, text="Go to Messages", command="").grid(row=12, column=4, columnspan=2)
          a_btn = Button(self, text="Go to Calendar", command="").grid(row=12, column=6, columnspan=2)
          a_btn = Button(self, text="Edit Profile", command="").grid(row=12, column=8,columnspan=2)
          #Buttons Row 2
          b_btn = Button(self, text="Wish Lists", command="").grid(row=13, column=4, columnspan=2)
          b_btn = Button(self, text="Gifts Purchased", command="").grid(row=13, column=6, columnspan=2)
          b_btn = Button(self, text="Shopping List", command="").grid(row=13, column=8, columnspan=2)
     
          #Wish List Area
          a_lbl = Label(self, text="My Wish List", font=("Arial Bold",15), justify=CENTER).grid(row=14, \
                         column=0, columnspan=16)
          a_lbl = Label(self, text="Last modified by "+mod.get("who")+" "+" on "+mod.get("date"), \
                        anchor=W).grid(row=15, column=0, columnspan=8, sticky=W)
          a_lbl = Label(self, text="Alternate Wish List Site(s): "+user.get("altwsh1"), \
                        anchor=W).grid(row=16, column=0, columnspan=8, sticky=W)
          #table head
          a_lbl = Label(self,text="Action", relief="raised", justify=CENTER).grid(row=18, column=1)
          b_lbl = Label(self,text="Description", relief="raised", justify=CENTER, width=100).grid(row=18, \
                        column=2, columnspan=11)
          c_lbl = Label(self,text="Desired", relief="raised", justify=CENTER, width=8).grid(row=18, column=13)
          d_lbl = Label(self, text="Expires", relief="raised", justify=CENTER, width=15).grid(row=18, column=14)
          #table
          for i in range(1,15,1):
               a_btn = Button(self, text="Edit", command="").grid(row=19+i , column=1)
               wdesc = Label(self, text=wsh[i]["des"], width=100, anchor=W, \
                             relief="sunken").grid(row=19+i,column=2, columnspan=11)
               wdes = Label(self, text=wsh[i]["ndes"], justify=CENTER, width=8, \
                            relief="sunken").grid(row=19+i,column=13)
               wexp = Label(self, text=wsh[i]["exp"], justify=CENTER, relief="sunken", \
                             width=15).grid(row=19+i,column=14)
               fil = Label(self, text=" ", relief="flat", width=5).grid(row=19+i,column=15)
          
          #Bottom Buttons
          self.pack()

def main():

    root = Tk()
    app = UHomePage()
    root.mainloop()


if __name__ == '__main__':
    main()
