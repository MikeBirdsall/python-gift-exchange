#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader

{# page input #}
payg = dict(action="Single", owner="Edward Birdsall", reason="display")

{# tab and header #}
hd = {"loc": "Select{{ payg.action }} Wish Lists"}
hdr = dict(name={{ payg.owner }}, page="Select {{ payg.action }} Wish Lists", today="Wednesday  March 06, 2019")

{# block1 #}
users = [
    dict(clan="Birdsall", id="alexahodgins", dname="Alexa Hodgins"),
    dict(clan="Birdsall", id="amari", dname="Amari Reich"),
    dict(clan="Birdsall", id="amy", dname="Amy Palma"),
    dict(clan="Birdsall, Kirkup", id="benjamin", dname="Benjamin Birdsall"),
    dict(clan="Birdsall", id="blaine", dname="Blaine Vernal"),
    dict(clan="Birdsall", id="brayden", dname="Brayden Reich"),
    dict(clan="Birdsall", id="bryan", dname="Bryan Kovas"),
    dict(clan="Kirkup", id="bryan", dname="Dan Kirkup"),
    dict(clan="Birdsall", id="derek", dname="Derek Birdsall"),
    dict(clan="Kirkup", id="derr", dname="Derrick Kirkup"),
    dict(clan="Birdsall", id="diane", dname="Diane Vernal"),
    dict(clan="Birdsall", id="ed", dname="Edward Birdsall"),
    dict(clan="Birdsall", id="erilyn", dname="Erilyn Kovas"),
    dict(clan="Birdsall", id="erin", dname="Erin Birdsall"),
    dict(clan="Birdsall", id="greg", dname="Greg Kovas"),
    dict(clan="Birdsall", id="greg1", dname="Greg Hodgins"),
    dict(clan="Birdsall", id="helen", dname="Helen Birdsall"),
    dict(clan="Birdsall", id="jim", dname="James Kovas"),
    dict(clan="Birdsall", id="junior", dname="Junior Palma"),
    dict(clan="Kirkup", id="sally", dname="Madeline Kirkup"),
    dict(clan="Birdsall, Kirkup", id="mike", dname="Michael Gerald Birdsall"),
    dict(clan="Birdsall", id="mike2", dname="Michael James Birdsall"),
    dict(clan="Kirkup", id="mikek", dname="Mike Kirkup"),
    dict(clan="Kirkup", id="mikel", dname="Mike LaFever"),
    dict(clan="Kirkup", id="norma", dname="Norma LaFever"),
    dict(clan="Birdsall", id="pat", dname="Patrick Birdsall"),
    dict(clan="Birdsall", id="peg", dname="Peg Kovas"),
    dict(clan="Birdsall", id="bob", dname="Robert Birdsall"),
    dict(clan="Birdsall", id="sandy", dname="Sandy Walker-Birdsall"),
    dict(clan="Birdsall, Kirkup", id="sue", dname="Susan Kirkup"),
    dict(clan="Birdsall", id="teresa", dname="Teresa Kovas"),
    dict(clan="Kirkup", id="wade", dname="Wade LaFever"),
    dict(clan="Birdsall", id="wesley", dname="Wesley Kovas")
]




input_ = {"hd":hd, "hdr":hdr, "users":users,  "payg":payg }

env = Environment(loader = FileSystemLoader("."))
template=env.get_template("UserHome.jhtml")


output = template.render(input_)

print(output)