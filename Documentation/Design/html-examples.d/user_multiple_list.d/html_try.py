#!/bin/python3

from jinja2 import Environment, FileSystemLoader

hd = {"loc":"Wish List"}
hdr = { "name":"Edward",  "page":" Multiple Wish List", "today":"Saturday  March  2, 2019" }


mod = {"who":"owner Edward Birdsall", "date":"Sunday Fed 24, 2019  13:15:12"}

wsh = [
    dict(num=1, pfor="Amy", ndes="any", exp="never",
         des="Frangelico, B&B, Irish Mist"),
    dict(num=2, pfor="Amy", ndes="any", exp="never",
         des="Fudge - chocolate, peanut butter are favorites"),
    dict(num=3, pfor="Amy", ndes="any", exp="never",
         des="Wine - Favorites yellowtail-*, wallaby creek-*, and others"),
    dict(num=4, pfor="Amy", ndes="any", exp="never",
         des="Gift Certificate - Home Depot or Lowes"),
   dict(num=1, pfor="Amy", ndes="any", exp="never",
         des="Frangelico, B&B, Irish Mist"),
   dict(num=-1, pfor=""),
    dict(num=5, pfor="Robert", ndes="any", exp="never",
         des="Gift Certificate - Barnes and Noble"),
    dict(num=6, pfor="Robert", ndes="any", exp="never",
         des="Gift Certificate - Right Stuf (www.rightstuf.com) (Where I get most of my anime and shaw dvds)"),
    dict(num=7, pfor="Robert", ndes="-1",
         des="Rasberry Pi Starter/learning kit", exp="Dec 26, 2019"),
    dict(num=8, pfor="Robert", ndes="any", exp="never",
         des="Candle molds especially for the larger candles (larger than votive) "),
   dict(num=-1, pfor=""),
    dict(num=9, pfor="Mike J", ndes="any", exp="Dec 26, 2019",
         des="washable long ties for church (not dryclean) looking for ties with primary color rose, white."),
    dict(num=10, pfor="Mike J", ndes="0", exp="Dec 26, 2019",
         des="CD by The Fire - Inspired (found at store.cdbaby.com)"),
    dict(num=11, pfor="Mike J", ndes="any", exp="Dec 26, 2020",
         des="Short sleeve Shirts 16 neck in red, rose, green, violet - liturgical colors to wear to church (same as ties)"),
    dict(num=12, pfor="Mike J", ndes="any", exp="Dec 26, 2020",
         des="Washable Ties in red, rose, green, violet - (liturgical colors to wear to church)"),
   dict(num=-1, pfor=""),
    dict(num=13, pfor="Derek", ndes="1", exp="Sep 01, 2019",
         des="Wishlist in final test mode"),
   dict(num=-1, pfor=""),
    dict(num=14, pfor="Wesley", ndes="1",
         des="2450 Canyon Sold", exp="Aug 1, 2019"),
   dict(num=-1, pfor=""),
    dict(num=15, pfor="Erilyn", ndes="1", exp="Dec 31, 2020",
         des="New House in 'Georgia")
]




input_ = {"hd":hd, "hdr":hdr, "mod":mod, "wsh":wsh  }
env = Environment(loader = FileSystemLoader("."))
template=env.get_template("multiplewish.jhtml")

output = template.render(input_ )

print(output)

