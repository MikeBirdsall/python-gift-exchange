#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader

# page input
#page = dict(action="single", user="Edward Birdsall")

# tab and header
hd = {"loc": "Shopping List Generation"}
hdr = dict(name="Ed", page="Shopping List Generation ", today="Wednesday  March 06, 2019")

# block1 dicts
# block 1 is the listing of all users and their shopping lists
wsh = [
    dict(num=1, pfor="Amy", ndes="any", exp="never",
         des="Frangelico, B&B, Irish Mist"),
    dict(num=2, pfor="Amy", ndes="any", exp="never",
         des="Fudge - chocolate, peanut butter are favorites"),
    dict(num=3, pfor="Amy", ndes="any", exp="never",
         des="Wine - Favorites yellowtail-*, wallaby creek-*, and others"),
    dict(num=4, pfor="Amy", ndes="any", exp="never",
         des="Gift Certificate - Home Depot or Lowes"),
   dict(num=5, pfor="Amy", ndes="any", exp="never",
         des="Craft beer"),
   dict(num=-1, pfor=""),
    dict(num=6, pfor="Robert", ndes="any", exp="never",
         des="Gift Certificate - Barnes and Noble"),
    dict(num=7, pfor="Robert", ndes="any", exp="never",
         des="Gift Certificate - Right Stuf (www.rightstuf.com) (Where I get most of my anime and shaw dvds)"),
    dict(num=8, pfor="Robert", ndes="1",
         des="Rasberry Pi Starter/learning kit", exp="Dec 26, 2019"),
    dict(num=9, pfor="Robert", ndes="any", exp="never",
         des="Candle molds especially for the larger candles (larger than votive) "),
   dict(num=-1, pfor=""),
    dict(num=10, pfor="Mike J", ndes="any", exp="Dec 26, 2019",
         des="washable long ties for church (not dryclean) looking for ties with primary color rose, white."),
    dict(num=11, pfor="Mike J", ndes="1", exp="Dec 26, 2019",
         des="CD by The Fire - Inspired (found at store.cdbaby.com)"),
    dict(num=12, pfor="Mike J", ndes="any", exp="Dec 26, 2020",
         des="Short sleeve Shirts 16 neck in red, rose, green, violet - liturgical colors to wear to church (same as ties)"),
    dict(num=13, pfor="Mike J", ndes="any", exp="Dec 26, 2020",
         des="Washable Ties in red, rose, green, violet - (liturgical colors to wear to church)"),
   dict(num=-1, pfor=""),
    dict(num=14, pfor="Derek", ndes="1", exp="Sep 01, 2019",
         des="Wishlist in final test mode"),
   dict(num=-1, pfor=""),
    dict(num=15, pfor="Wesley", ndes="1",
         des="http://Amazon.com/....", exp="Aug 1, 2019"),
   dict(num=-1, pfor=""),
    dict(num=16, pfor="Erilyn", ndes="1", exp="Dec 31, 2020",
         des="http://Amazon.com/...."),
    dict(num=17, pfor="Erilyn", ndes="1", exp="Dec 31, 2020",
         des="Towel with Ariel")
]
#------------------------------------------------------------------------------------------------------------------------------------------------------
# block2 dicts

#------------------------------------------------------------------------------------------------------------------------------------------------------

# block3 dicts

# collect all the dicts and such
input_ = {"hd":hd, "hdr":hdr, "wsh":wsh}

# now to go out and render

env = Environment(loader = FileSystemLoader("../templates/"))
template=env.get_template("shop_list_gen.jhtml")


output = template.render(input_)

print(output)