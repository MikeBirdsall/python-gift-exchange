#!/bin/python3

from jinja2 import Environment, FileSystemLoader

hd = {"loc":"Wish List"}
hdr = { "name":"Edward",  "page":" Wish List", "today":"Saturday  March  2, 2019" }


# devt is intended to hold the number of events for the day to be used in the template with an if or for but can't get to work right now

mod = {"who":"owner Edward Birdsall", "date":"Sunday Fed 24, 2019  13:15:12"}

wsh = [
    dict(num=1, ndes="any", exp="never",
         des="Frangelico, B&B, Irish Mist"),
    dict(num=2, ndes="any", exp="never",
         des="Fudge - chocolate, peanut butter are favorites"),
    dict(num=3, ndes="any", exp="never",
         des="Wine - Favorites yellowtail-*, wallaby creek-*, and others"),
    dict(num=4, ndes="any", exp="never",
         des="Gift Certificate - Home Depot or Lowes"),
    dict(num=5, ndes="any", exp="never",
         des="Gift Certificate - Barnes and Noble"),
    dict(num=6, ndes="any", exp="never",
         des=("Gift Certificate - Right Stuf (www.rightstuf.com) Where I get "
              "most of my anime and shaw dvds")),
    dict(num=7, ndes="-1",
         des="Rasberry Pi Starter/learning kit", exp="Dec 26, 2019"),
    dict(num=8, ndes="any", exp="never",
         des=("Candle molds especially for the larger candles (larger than "
             "votive)")),
    dict(num=9, ndes="any", exp="Dec 26, 2019",
         des=("washable long ties for church (not dryclean) looking for ties "
             "with primary color rose, white.")),
    dict(num=10, ndes="0", exp="Dec 26, 2019",
         des="CD by The Fire - Inspired (found at store.cdbaby.com)"),
    dict(num=11, ndes="any", exp="Dec 26, 2020",
         des=("Short sleeve Shirts 16 neck in red, rose, green, violet - "
              "liturgical colors to wear to church (same as ties)")),
    dict(num=12, ndes="any", exp="Dec 26, 2020",
         des=("Washable Ties in red, rose, green, violet - liturgical colors to wear to church")),
    dict(num=13, ndes="1", exp="Sep 01, 2019",
         des="Wishlist in final test mode"),
    dict(num=14, ndes="1",
         des="2450 Canyon Sold", exp="Aug 1, 2019"),
    dict(num=15, ndes="1", exp="Dec 31, 2020",
         des="New House in 'Georgia"),
]

item = dict(description="Washable Ties in red, rose, green, violet - liturgical colors to wear to church", 
     desired="any", avail="any", exp="Dec 26, 2020", notes="green and red bought", submitted="Edward Birdsall",
      purch="e-mail", group="e-mail", submitter="e-mail", buy="yes",reserve="yes"  )



input_ = {"hd":hd, "hdr":hdr, "mod":mod, "wsh":wsh, "item":item }
env = Environment(loader = FileSystemLoader("."))
template=env.get_template("singlewish.html")

output = template.render(input_ )

print(output)

