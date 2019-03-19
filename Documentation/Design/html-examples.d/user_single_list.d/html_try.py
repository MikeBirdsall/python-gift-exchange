#!/bin/python3

from jinja2 import Environment, FileSystemLoader
import sys

hd = {"loc":"Wish List"}
hdr = { "name":"Edward",  "page":" Wish List", "today":"Saturday  March  2, 2019" }


# devt is intended to hold the number of events for the day to be used in the template with an if or for but can't get to work right now
# sys.argv[1] may equal the owner "Edward Birdsall" or someone else
# sys.argv[2] may equal "Detail" to show item detail or anything else to show nothing
if len(sys.argv) == 3 and sys.argv[2] == "Detail":
     payg = dict(action="Detail",viewer=sys.argv[1], owner="Edward Birdsall")
else:
     payg = dict(action="No Detail",viewer=sys.argv[1], owner="Edward Birdsall")


mod = {"who":"owner Edward Birdsall", "date":"Sunday Fed 24, 2019  13:15:12"}

wsh = [
    dict(num=1, ndes="any", avail="any", exp="never",
         des="Frangelico, B&B, Irish Mist", submitter="Edward Birdsall" ),
    dict(num=2, ndes="any",  avail="any",exp="never",
         des="Fudge - chocolate, peanut butter are favorites", submitter="Edward Birdsall" ),
    dict(num=3, ndes="any",  avail="any",exp="never",
         des="Wine - Favorites yellowtail-*, wallaby creek-*, and others", submitter="Edward Birdsall" ),
    dict(num=4, ndes="any", avail="any", exp="never",
         des="Gift Certificate - Home Depot or Lowes", submitter="Edward Birdsall" ),
    dict(num=5, ndes="any",  avail="any",exp="never",
         des="Gift Certificate - Barnes and Noble", submitter="Edward Birdsall" ),
    dict(num=6, ndes="any",  avail="any",exp="never",
         des=("Gift Certificate - Right Stuf (www.rightstuf.com) Where I get "
              "most of my anime and shaw dvds"), submitter="Edward Birdsall" ),
    dict(num=7, ndes="1", avail="-1",
         des="Rasberry Pi Starter/learning kit", exp="Dec 26, 2019", submitter="Michael Birdsall" ),
    dict(num=8, ndes="any",  avail="any",exp="never",
         des=("Candle molds especially for the larger candles (larger than "
             "votive)"), submitter="Edward Birdsall" ),
    dict(num=9, ndes="any",  avail="any", exp="Dec 26, 2019",
         des=("washable long ties for church (not dryclean) looking for ties "
             "with primary color rose, white."), submitter="Edward Birdsall" ),
    dict(num=10, ndes="1",  avail="0", exp="Dec 26, 2019",
         des="CD by The Fire - Inspired (found at store.cdbaby.com)", submitter="Edward Birdsall" ),
    dict(num=11, ndes="any",  avail="any", exp="Dec 26, 2020",
         des=("Short sleeve Shirts 16 neck in red, rose, green, violet - "
              "liturgical colors to wear to church (same as ties)"), submitter="Edward Birdsall" ),
    dict(num=12, ndes="any",  avail="any", exp="Dec 26, 2020",
         des=("Washable Ties in red, rose, green, violet - liturgical colors to wear to church"), submitter="Edward Birdsall" ),
    dict(num=13, ndes="1",  avail="1", exp="Sep 01, 2019",
         des="Wishlist in final test mode", submitter="Edward Birdsall" ),
    dict(num=14, ndes="1", avail="1",
         des="2450 Canyon Sold", exp="Aug 1, 2019", submitter="Edward Birdsall" ),
    dict(num=15, ndes="1",  avail="1",exp="Dec 31, 2020",
         des="New House in 'Georgia", submitter="Edward Birdsall" ),
]

item = dict(description="Washable Ties in red, rose, green, violet - liturgical colors to wear to church", 
     desired="any", avail="any",npurch=3, exp="Dec 26, 2020", notes="green and red bought", submitted="Edward Birdsall",
      purch="e-mail", group="e-mail", submitter="e-mail", buy="yes",reserve="yes"  )
altwsh = dict(syte="http://Amazon_site_url")


input_ = {"hd":hd, "hdr":hdr, "mod":mod, "wsh":wsh, "item":item, "altwsh":altwsh, "payg":payg }
env = Environment(loader = FileSystemLoader("../templates/"))
template=env.get_template("singlewish.jhtml")

output = template.render(input_ )

print(output)

