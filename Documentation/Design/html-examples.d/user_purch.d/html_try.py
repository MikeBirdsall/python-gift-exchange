#!/bin/python3

from jinja2 import Environment, FileSystemLoader

hd = {"loc":"Purchased List"}
hdr = { "name":"Edward",  "page":" Purchased List", "today":"Saturday  March  2, 2019  13:29:15" }



pers = dict(clan="Birdsall", yr="2018", sspk="Robert Birdsall", event="Christmas")


wsh = [
    dict(num=1, pfor="Amy Kovas", ndes="1", notes="",
         des="Psych: Season 4 (TV Series)"),
    dict(num=2, pfor="Benjamin Birdsall", ndes="1", notes="set #10232",
         des="legos"),
    dict(num=3, pfor="Robert Birdsall", ndes="1", notes="Home Depot",
         des="Gift card for Lowe's or Home Depot"),
    dict(num=4, pfor="Robert Birdsall", ndes="1", notes="Lowe",
         des="Gift Certificate - Home Depot or Lowes"),
    dict(num=5, pfor="Bryan Kovas", ndes="1", notes="",
         des="CD - Linkin Park: A Thousand Suns"),
    dict(num=6, pfor="Derek Birdsall", ndes="2", notes="",
         des="Hot Wheels or Matchbox Cars"),
    dict(num=7, pfor="Erin Birdsall", ndes="1",
         des="Celtic Woman or Celtic Thunder Cds", notes="Celtic Thundar"),
    dict(num=8, pfor="Greg Kovas", ndes="1", notes="",
         des="CD: Default - Comes and Goes"),
    dict(num=9, pfor="Erilyn Kovas", ndes="", notes="",
         des=""),
    dict(num=10, pfor="Wesley Kovas", ndes="", notes="",
         des=""),
]


input_ = {"hd":hd, "hdr":hdr,  "wsh":wsh, "pers":pers }
env = Environment(loader = FileSystemLoader("."))
template=env.get_template("user_purch.html")

output = template.render(input_ )

print(output)

