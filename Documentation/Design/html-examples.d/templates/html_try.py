#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader

# page input
page = dict(action="single", user="Edward Birdsall")

# tab and header
hd = {"loc": "Pick"}
hdr = dict(name="Ed", page="Pick ", today="Wednesday  March 06, 2019")

#block1 dicts

# block2 dicts

# block3 dicts

# collect all the dicts and such
input_ = {"hd":hd, "hdr":hdr, "user":user, "msgs":msgs , "ss":ss, "evt":evt, "mod":mod, "wsh":wsh }

# now to go out and render

env = Environment(loader = FileSystemLoader("."))
template=env.get_template("UserHome.jhtml")


output = template.render(input_)

print(output)