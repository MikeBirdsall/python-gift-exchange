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
          mod = {"who":"owner Edward Birdsall", "date":"Sunday Fed 24, 2019  13:15:12"}
          wsh = [
               dict(num=1, ndes="any", exp="never", des="Frangelico, B&B, Irish Mist"),
               dict(num=2, ndes="any", exp="never", des="Fudge - chocolate, peanut butter are \
                    favorites"),
               dict(num=3, ndes="any", exp="never", des="Wine - Favorites yellowtail-*, wallaby \
                    creek-*, and others"),
               dict(num=4, ndes="any", exp="never", des="Gift Certificate - Home Depot or Lowes"),
               dict(num=5, ndes="any", exp="never", des="Gift Certificate - Barnes and Noble"),
               dict(num=6, ndes="any", exp="never", des=("Gift Certificate - Right Stuf \
                    (www.rightstuf.com) Where I get most of my anime and shaw dvds")),
               dict(num=7, ndes="1",   des="Rasberry Pi Starter/learning kit", exp="Dec 26, 2019"),
               dict(num=8, ndes="any", exp="never", des=("Candle molds especially for the larger \
                    candles (larger than votive)")),
               dict(num=9, ndes="any", exp="Dec 26, 2019", des=("washable long ties for church \
                    (not dryclean) looking for ties with primary color rose, white.")),
               dict(num=10, ndes="1", exp="Dec 26, 2019", des="CD by The Fire - Inspired (found at\
                    store.cdbaby.com)"),
               dict(num=11, ndes="any", exp="Dec 26, 2020", des=("Short sleeve Shirts 16 neck in \
                    red, rose, green, violet - liturgical colors to wear to church (same as ties)")),
               dict(num=12, ndes="any", exp="Dec 26, 2020", des=("Washable Ties in red, rose, green,\
                    violet - liturgical colors to wear to church")),
               dict(num=13, ndes="1", exp="Sep 01, 2019", des="Wishlist in final test mode"),
               dict(num=14, ndes="1", des="2450 Canyon Sold", exp="Aug 1, 2019"),
               dict(num=15, ndes="1", exp="Dec 31, 2020", des="New House in 'Georgia"),
               ]

          #========================================================================================
          #Ending of definitions.  Need to remember how to split this into a seperate area that
          # invokes MCalendar
          #========================================================================================
          #Window Display
          self.master.title(hd.get("loc"))
          ht0 = Label(self,text=hdr.get("name")+"'s "+hdr.get("page"), justify=CENTER, relief="flat", 
                      background="lightblue").grid(row=0, columnspan=16, sticky=W+E)
          ht1 = Label(self, text="", relief="flat", padx=150, fg="lightblue", \
                      bg="lightblue").grid(row=1, rowspan=2, column=0, columnspan=16)
          ht2 = Label(self,text="Today's Date: "+hdr.get("today") , justify=CENTER, relief="flat", \
                      background="lightblue").grid(row=3, columnspan=16, sticky=W+E) 
          #Header Display
          hdr_1 = Label(self, text="Information", justify=LEFT).grid(row=4, column=0)
          hdr_2 = Label(self, text="Personal", justify=LEFT).grid(row=5, column=0)
          hdr_30 = Label(self, text="Full Name:", justify=CENTER).grid(row=6, column=0)
          hdr_31 = Label(self, text=user.get("firstn")+" "+user.get("lastn"), \
                        justify=RIGHT).grid(row=6, column=1, columnspan=2)
          hdr_31 = Label(self, text="Birthday: "+user.get("bmn")+" "+user.get("bday")+", "+user.get("byr"), \
                         justify=CENTER).grid(row=6, column=3)
          hdr_32 = Label(self, text="e-mail: "+user.get("pemail")+"   "+user.get("semail"), \
                         justify=CENTER).grid(row=6, column=4, columnspan=9)
          
          #Buttons Row 1
          #Buttons Row 2
         
          #ct1 = 
          #ct2
          #ct3
          #Wish List Area
         
          #table head
          a_lbl = Label(self,text="Action", relief="raised", justify=CENTER).grid(row=13, column=1)
          b_lbl = Label(self,text="Description", relief="raised", justify=CENTER,width=100).grid(row=13, \
                        column=2, columnspan=11)
          c_lbl = Label(self,text="Desired", relief="raised", justify=CENTER, width=8).grid(row=13, column=13)
          d_lbl = Label(self, text="Expires", relief="raised", justify=CENTER, width=15).grid(row=13, column=14)
          #table
          for i in range(1,12,1):
               a_btn = Button(self, text="Edit", command="").grid(row=14+i , column=1)
               wdesc = Label(self, text=wsh[i]["des"], width=100, anchor=W, \
                             relief="sunken").grid(row=14+i,column=2, columnspan=11)
               wdes = Label(self, text=wsh[i]["ndes"], justify=CENTER, width=8, \
                            relief="sunken").grid(row=14+i,column=13)
               wexp = Label(self, text=wsh[i]["exp"], justify=CENTER, relief="sunken", \
                             width=15).grid(row=14+i,column=14)
               fil = Label(self, text=" ", relief="flat", width=5).grid(row=14+1,column=15)
          
          #Bottom Buttons
          self.pack()

def main():

    root = Tk()
    app = UHomePage()
    root.mainloop()


if __name__ == '__main__':
    main()
