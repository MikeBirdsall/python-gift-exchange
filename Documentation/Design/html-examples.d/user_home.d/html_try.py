#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader

hd = {"loc": "User Home"}
hdr = { "name": "Ed",  "page":"Home", "today":"Wednesday  March 06, 2019" }

user = {"firstn":"Edward", "lastn":"Birdsall", "bday":"23", "byr":"1952", "bmn":"April", "pemail":"birdsall_99@comcast.net", "semail":"ntdgn@umich.edu", "clan":"Birdsall" }
msgs = {"new":0, "tot":10}
ss = {"cyr":2018, "cypk":"Peggy Kovas" }
evt = {"event1": "None", "bday1":"Mar 17 - Terri McIntosh", "bday2":"Mar 29 - Alexa Hodgins"}
mod = {"who":"owner Edward Birdsall", "date":"Sunday Fed 24, 2019  13:15:12"}

wsh = []
for i in range(0, 16, 1):
     wsh.append({"num":i, "ndes":"1","des":"","exp":""})

wsh[1]["ndes"] = "any"
wsh[1]["des"] = "Frangelico, B&B, Irish Mist"
wsh[1]["exp"] = "never"
wsh[2]["ndes"] = "any"
wsh[2]["des"] = "Fudge - chocolate, peanut butter are favorites"
wsh[2]["exp"] = "never"
wsh[3]["ndes"] = "any"
wsh[3]["des"] = "Wine - Favorites yellowtail-*, wallaby creek-*, and others"
wsh[3]["exp"] = "never"
wsh[4]["ndes"] = "any"
wsh[4]["des"] = "Gift Certificate - Home Depot or Lowes"
wsh[4]["exp"] = "never"
wsh[5]["ndes"] = "any"
wsh[5]["des"] = "Gift Certificate - Barnes and Noble"
wsh[5]["exp"] = "never"
wsh[6]["ndes"] = "any"
wsh[6]["des"] = "Gift Certificate - Right Stuf (www.rightstuf.com) Where I get most of my anime and shaw dvds"
wsh[6]["exp"] = "never"
wsh[7]["ndes"] = "1"
wsh[7]["des"] = "Rasberry Pi Starter/learning kit"
wsh[7]["exp"] = "Dec 26, 2019"
wsh[8]["ndes"] = "any"
wsh[8]["des"] = "Candle molds especially for the larger candles (larger than votive)"
wsh[8]["exp"] = "never"
wsh[9]["ndes"] = "any"
wsh[9]["des"] = "washable long ties for church (not dryclean) looking for ties with primary color rose, white."
wsh[9]["exp"] = "Dec 26, 2019"
wsh[10]["ndes"] = "1"
wsh[10]["des"] = "CD by The Fire - Inspired (found at store.cdbaby.com)"
wsh[10]["exp"] = "Dec 26, 2019"
wsh[11]["ndes"] ="any"
wsh[11]["des"] = "Short sleeve Shirts 16 neck in red, rose, green, violet - liturgical colors to wear to church (same as ties)"
wsh[11]["exp"] = "Dec 26, 2020"
wsh[12]["ndes"] = "any"
wsh[12]["des"] = "Washable Ties in red, rose, green, violet - liturgical colors to wear to church"
wsh[12]["exp"] = "Dec 26, 2020"
wsh[13]["ndes"] = "1"
wsh[13]["des"] = "Wishlist in final test mode"
wsh[13]["exp"] = "Sep 01, 2019"
wsh[14]["ndes"] = "1"
wsh[14]["des"] = "2450 Canyon Sold"
wsh[14]["exp"] = "Aug 01, 2019"
wsh[15]["ndes"] = "1"
wsh[15]["des"] = "New House in Gerogia"
wsh[15]["exp"] = "Dec 31, 2020"






input_ = {"hd":hd, "hdr":hdr, "user":user, "msgs":msgs , "ss":ss, "evt":evt, "mod":mod, "wsh":wsh }

env = Environment(loader = FileSystemLoader("."))
template=env.get_template("UserHome.html")


output = template.render(input_)

print(output)