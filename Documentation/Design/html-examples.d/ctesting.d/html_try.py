#!/usr/bin/python3
#
from jinja2 import Environment, FileSystemLoader

{# page input #}
 payg = {"action":"Single", "owner":"Edward Birdsall", "reason":"display"}
     {#actions "Single" Multiple"  reason "display" "Shopping List"
{# tab and header #}
hd = {"loc": "Select "+payg['action']+" Wish Lists"}
hdr = {"name":payg['owner'], "page":"Select "+ payg['action']+" Wish Lists", "today":"Wednesday  March 06, 2019"}
#}
{# block1 #}

users = [ 
     {"clan":"Birdsall", "id":"alexahodgins", "dname":"Alexa Hodgins"},
    {"clan":"Birdsall", "id":"amari", "dname":"Amari Reich"},
    {"clan":"Birdsall", "id":"amy", "dname":"Amy Palma"},
    {"clan":"Birdsall, Kirkup", "id":"benjamin", "dname":"Benjamin Birdsall"},
    {"clan":"Birdsall", "id":"blaine", "dname":"Blaine Vernal"},
    {"clan":"Birdsall", "id":"brayden", "dname":"Brayden Reich"},
    {"clan":"Birdsall", "id":"bryan", "dname":"Bryan Kovas"},
    {"clan":"Kirkup", "id":"bryan", "dname":"Dan Kirkup"},
    {"clan":"Birdsall", "id":"derek", "dname":"Derek Birdsall"},
    {"clan":"Kirkup", "id":"derr", "dname":"Derrick Kirkup"},
    {"clan":"Birdsall", "id":"diane", "dname":"Diane Vernal"},
    {"clan":"Birdsall", "id":"ed", "dname":"Edward Birdsall"},
    {"clan":"Birdsall", "id":"erilyn", "dname":"Erilyn Kovas"},
    {"clan":"Birdsall", "id":"erin", "dname":"Erin Birdsall"},
    {"clan":"Birdsall", "id":"greg", "dname":"Greg Kovas"},
    {"clan":"Birdsall", "id":"greg1", "dname":"Greg Hodgins"},
    {"clan":"Birdsall", "id":"helen", "dname":"Helen Birdsall"},
    {"clan":"Birdsall", "id":"jim", "dname":"James Kovas"},
    {"clan":"Birdsall", "id":"junior", "dname":"Junior Palma"},
    {"clan":"Kirkup", "id":"sally", "dname":"Madeline Kirkup"},
    {"clan":"Birdsall, Kirkup", "id":"mike", "dname":"Michael Gerald Birdsall"},
    {"clan":"Birdsall", "id":"mike2", "dname":"Michael James Birdsall"},
    {"clan":"Kirkup", "id":"mikek", "dname":"Mike Kirkup"},
    {"clan":"Kirkup", "id":"mikel", "dname":"Mike LaFever"},
    {"clan":"Kirkup", "id":"norma", "dname":"Norma LaFever"},
    {"clan":"Birdsall", "id":"pat", "dname":"Patrick Birdsall"},
    {"clan":"Birdsall", "id":"peg", "dname":"Peg Kovas"},
    {"clan":"Birdsall", "id":"bob", "dname":"Robert Birdsall"},
    {"clan":"Birdsall", "id":"sandy", "dname":"Sandy Walker-Birdsall"},
    {"clan":"Birdsall, Kirkup", "id":"sue", "dname":"Susan Kirkup"},
    {"clan":"Birdsall", "id":"teresa", "dname":"Teresa Kovas"},
    {"clan":"Kirkup", "id":"wade", "dname":"Wade LaFever"},
    {"clan":"Birdsall", "id":"wesley", "dname":"Wesley Kovas"}
]

print(users)




{#
input_ = {"hd":hd, "hdr":hdr, "users":users,  "payg":payg }

env = Environment(loader = FileSystemLoader("../templates/"))
template=env.get_template("user_pick_list.jhtml")


output = template.render(input_)

print(output) #}