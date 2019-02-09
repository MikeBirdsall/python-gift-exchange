#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader

hd = {"loc": "User Home"}
hdr = { "name": "Ed",  "page":"Home", "today":"Wednesday  March 06, 2019" }
user = {"firstn":"Edward", "lastn":"Birdsall", "bday":"23", "byr":"1952", "bmn":"April", "pemail":"birdsall_99@comcast.net", "semail":"ntdgn@umich.edu", "clan":"Birdsall" }
msgs = {"new":0, "tot":10}
ss = {"cyr":2018, "cypk":"Peggy Kovas" }






input_ = {"hd":hd, "hdr":hdr, "user":user, "msgs":msgs , "ss":ss }

env = Environment(loader = FileSystemLoader("."))
template=env.get_template("UserHome.html")


output = template.render(input_)

print(output)