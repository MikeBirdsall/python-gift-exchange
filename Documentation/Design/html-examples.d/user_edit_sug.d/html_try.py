#!/bin/python3

from jinja2 import Environment, FileSystemLoader
import sys

action = sys.argv[1]  # alternates are adding, verifying, editing and deleting
owner = dict(name="Edward Birdsall", moddate="Monday December 2, 2018 14:12:25")
submitter = dict(name=sys.argv[2], moddate="Monday December 2, 2018 14:12:25")
dayt = dict(today="March 2, 2019", maxday="2025-12-31")



# block 1
if action == "adding":
     hd = {"loc":"Add Suggestion"}
     hdr = { "name":"Edward",  "page":" Add Suggestion", "today":"Saturday  March  2, 2019  13:29:15" }
     twish = dict(num=16,  ndes="", exp="", des="", notes="")
elif action == "verifying" :
     hd = {"loc":"Verify Suggestion"}
     hdr = { "name":"Edward",  "page":" Verify Suggestion", "today":"Saturday  March  2, 2019  13:29:15" }
     twish = dict(num=7, submitn="Edward Birdsall", submitd="2019-01-05", ndes="1",
         des="Rasberry Pi Starter/learning kit", exp="Dec 26, 2019", notes="Some Note here")
elif action == "editing" :
     hd = {"loc":"Edit Suggestion"}
     hdr = { "name":"Edward",  "page":" Edit Suggestion", "today":"Saturday  March  2, 2019  13:29:15" }
     twish = dict(num=7, submitn="Edward Birdsall", submitd="2019-01-05", ndes="1",
         des="Rasberry Pi Starter/learning kit", exp="2019-12-26", notes="Some Note here")
elif action == "deleting" :
     hd = {"loc":"Delete Suggestion"}
     hdr = { "name":"Edward",  "page":" Delete Suggestion", "today":"Saturday  March  2, 2019  13:29:15" }
     twish = dict(num=7, submitn="Edward Birdsall", submitd="2019-01-05", ndes="1",
         des="Rasberry Pi Starter/learning kit", exp="Dec 26, 2019", notes="Some Note here")

else:
      hd = {"loc":"Lost in webspace"}

mod = {"owner":"Edward Birdsall","own-mod":"Monday December 2, 2018 14:12:25",
               "who":"Edward Birdsall", "date":"Sunday Fed 24, 2019  13:15:12"}
# block 2
wsh = [
    dict(num=1, submitn="Edward Birdsall", submitd="2019-01-05", ndes="any", exp="never",
         des="Frangelico, B&B, Irish Mist", notes="Some Note here", bc="White"),
    dict(num=2, submitn="Edward Birdsall", submitd="2019-01-05", ndes="any", exp="never",
         des="Fudge - chocolate, peanut butter are favorites", notes="Some Note here", bc="White"),
    dict(num=3, submitn="Edward Birdsall", submitd="2019-01-05", ndes="any", exp="never",
         des="Wine - Favorites yellowtail-*, wallaby creek-*, and others", notes="Some Note here", bc="White"),
    dict(num=4, submitn="Edward Birdsall", submitd="2019-01-05", ndes="any", exp="never",
         des="Gift Certificate - Home Depot or Lowes", notes="Some Note here", bc="White"),
    dict(num=5, submitn="Edward Birdsall", submitd="2019-01-05", ndes="any", exp="never",
         des="Gift Certificate - Barnes and Noble", notes="Some Note here", bc="White"),
    dict(num=6, submitn="Edward Birdsall", submitd="2019-01-05", ndes="any", exp="never",
         des=("Gift Certificate - Right Stuf (www.rightstuf.com) Where I get "
              "most of my anime and shaw dvds"), notes="Some Note here", bc="White"),
    dict(num=7, submitn="Edward Birdsall", submitd="2019-01-05", ndes="1",
         des="Rasberry Pi Starter/learning kit", exp="Dec 26, 2019", notes="Some Note here", bc="White"),
    dict(num=8, submitn="Edward Birdsall", submitd="2019-01-05", ndes="any", exp="never",
         des=("Candle molds especially for the larger candles (larger than "
             "votive)"), notes="Some Note here", bc="White"),
    dict(num=9, submitn="Edward Birdsall", submitd="2019-01-05", ndes="any", exp="Dec 26, 2019",
         des=("washable long ties for church (not dryclean) looking for ties "
             "with primary color rose, white."), notes="Some Note here", bc="White"),
    dict(num=10, submitn="Robert Birdsall", submitd="2019-01-05", ndes="1", exp="Dec 26, 2019",
         des="CD by The Fire - Inspired (found at store.cdbaby.com)", notes="Some Note here", bc="White"),
    dict(num=11, submitn="Edward Birdsall", submitd="2019-01-05", ndes="any", exp="Dec 26, 2020",
         des=("Short sleeve Shirts 16 neck in red, rose, green, violet - "
              "liturgical colors to wear to church (same as ties)"), notes="Some Note here", bc="White"),
    dict(num=12, submitn="Edward Birdsall", submitd="2019-01-05", ndes="any", exp="Dec 26, 2020",
         des=("Washable Ties in red, rose, green, violet - liturgical colors to wear to church"), notes="Some Note here", bc="White"),
    dict(num=13, submitn="Michael Birdsall", submitd="2019-01-05", ndes="1", exp="Sep 01, 2019",
         des="Wishlist in final test mode", notes="Some Note here", bc="White"),
    dict(num=14, submitn="Michael Birdsall", submitd="2019-01-05", ndes="1",
         des="2450 Canyon Sold", exp="Aug 1, 2019", notes="Some Note here", bc="White"),
    dict(num=15, submitn="Edward Birdsall", submitd="2019-01-05", ndes="1", exp="Dec 31, 2020",
         des="New House in 'Georgia", notes="Some Note here", bc="White")
]

for w in wsh:
     if w["num"] == twish["num"]:
          w["bc"]="Plum"


# block 3



input_ = {"hd":hd, "hdr":hdr,  "wsh":wsh, "action":action, "owner":owner, "submitter":submitter, "dayt":dayt, "mod":mod, "twish":twish}
env = Environment(loader = FileSystemLoader("../templates/"))
template=env.get_template("user_addedit_sug.jhtml")

output = template.render(input_ )

print(output)