#!/bin/python3

from jinja2 import Environment, FileSystemLoader

action = "adding" {# alternates are editing and deleting #}
owner = dict(name="Edward Birdsall", moddate="Monday December 2, 2018 14:12:25")
submitter = dict(name="Edward Birdsall",moddate="Monday December 2, 2018 14:12:25")
dayt = dict{today="2019-03-02", maxday="2025-12-31")

{% if action = "adding" %}
awish = dict(num=0, ndes="", exp="", des="", notes="", submitter="Edward Birdsall", date="March  2, 2019"
          owner="Edward Birdsall"}
{% elif action = "editing" %}
awish = dict(num=0, ndes="", exp="", des="", notes="", submitter="Edward Birdsall", date="March  2, 2019"
          owner="Edward Birdsall"}

{% elif action = "deleting" %}
{% else %}
{% endif %}

{# block 1 #}

{% if action = "add" %}
     hd = {"loc":"Add Suggestion"}
     hdr = { "name":"Edward",  "page":" Add Suggestion", "today":"Saturday  March  2, 2019  13:29:15" }
{% elif action = "edit" %}
     hd = {"loc":"Edit Suggestion"}
     hdr = { "name":"Edward",  "page":" Edit Suggestion", "today":"Saturday  March  2, 2019  13:29:15" }
{% elif action = "delete" %}
     hd = {"loc":"Delete Suggestion"}
     hdr = { "name":"Edward",  "page":" Delete Suggestion", "today":"Saturday  March  2, 2019  13:29:15" }
{% else %}
{% endif %}

mod = {"owner":"Edward Birdsall","own-mod":"Monday December 2, 2018 14:12:25",
               "who":"Edward Birdsall", "date":"Sunday Fed 24, 2019  13:15:12"}
{# block 2 #}
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

{# block 3 #}



input_ = {"hd":hd, "hdr":hdr,  "wsh":wsh, "pers":pers }
env = Environment(loader = FileSystemLoader("."))
template=env.get_template("addedit.jhtml")

output = template.render(input_ )

print(output)

