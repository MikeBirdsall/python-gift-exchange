#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader

# page input
page = dict(action="single", user="Edward Birdsall")

# tab and header
hd = {"loc": "Profile Edit"}
hdr = dict(name="Ed", page="Edit Profile ", today="Wednesday  March 06, 2019")

#block1 dicts
user = dict(fname="Edward Birdsall", dname="Ed Birdsall", bday="April 23, 1952", clan="Birdsall", 
     spouse="None", children="None", pemail="birdsall_99@comcast.net", semail="ntdgn@umich.edu",
     altwishsite="None", proxy="None" )
# block2 dicts

# block3 dicts

# collect all the dicts and such
input_ = {"hd":hd, "hdr":hdr, "user":user }

# now to go out and render

env = Environment(loader = FileSystemLoader("."))
template=env.get_template("user_edit_password.jhtml")


output = template.render(input_)

print(output)