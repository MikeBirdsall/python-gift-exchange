#!/usr/bin/python3
"""
     Site Init GUI for Wish List
"""
from tkinter import *

GREETINGS = """ Welcome
===============================================================================================
     Welcome to the Site Initialization of the Wish List program Version 0.999999

     Here you will set up a number of things needed to initialize the site for the program.
"""

TASK1 = """ Task 1 - Set up needed directories on ther Server
===============================================================================================
     The first task is to set up needed directories if not already done so.  You will first be
     asked for where the main directory for the website is to be.  I'll check to see if it
     already exists and if not create it.  Then I'll list needed directories and suggested
     locations for them.  After you have checked and verified them I'll create as necessary the
     needed directories.
"""

TASK2 = """ Task 2 - Transfer information to the directories and begin to customize site
===============================================================================================
     Now I'll populate the directories with standard information and code and then begin to
     customize this new web site with information from you.  The first bits of information will
     be about you, the owner, and the site in general.
"""


LARGE_FONT = ("Times", 12)
NORMAL_FONT = ("Times", 10)
SMALL_FONT = ("Times", 8)


class CreateUser():
     """
     Tk screen to Create a User and set in initial vaues.  An alternate to the HTML page
     to create a user and would normally be used to inially set up the Owner and perhaps
     some of the administrators. 
     """
     #FIXME:CreateUser: Set up to be called with a file as an argument to load in a file of users?
     pass

class CreateGroup():
     """
     Tk screen to Create a Group and set in inital values.  An alternative to the HTML page
     to create a group and would noramlly be used to set up initial groups for site, owner and
     other initial groups desired.
     """
     pass

class TkPage(Tk):
     """
     Sets up a standard Tk page for use in this program
     """

     def __init__(self, *args, **kwargs):

          Tk.__init__(self, *args, **kwargs)
          self.geometry('1600x1800')
          #FIXME: TkPage - have an Icon for the program?  if so, need to create

          self.title('Wish List Site Initialization')
          #self.iconbitmap('@./py-blue-trans-out.xbm')
          #FIXME: SiteInit - have an Icon for the program?  if so, need to create

class InitializeSite(TkPage):
     """
     Tk screen(s) to welcome the new Owner and co-ordinate the setting up the site.
     First call before Mainloop of program to set up site.  Should set up something so that
     program can tell if program/site has been initialized.
     """
     #TODO: SiteInit - Window size set to 3/4 screen height and width

     """
     Define a table with ordered tasks, a button do do the task and a box that is checked when done.
          Required Tasks
     Next define a table of optional tasks that can be done at initialization to further set up 
     the site before activating the website.
     #Tasks
     #Task 1 - Greet Owner
     #task 1a - ask for Location of website on server
     #task 1b - ask for location of database on server
     #task 1c - ask for location of code on server
     #task 1_ _ ask for location for ___ on server
     #task 1_ - setup directories for website
     #Task 2 - init databases
     #task 2a - init the database and other things as needed
     #task 2b - transfer information the directotries to set up the site
     #task 2c - begin customization for the site installation
     #task 2c1 - master user Information
     #task 2d - get website webpages customization information
     #task 2d1 - header customization
     #task 2d2 - footer customization
     #task 2d3 - body customization
     #task 5 - init website
     Bottom should have buttons for
     """

     def __init__(self, *args, **kwargs):
          Tk.__init__(self, *args, **kwargs)
     """
          MAKE THIS SIMPLE -- EACH PAGE IS A SUBSET OF TkPage
          DON'T MIX Container and grid unless desireable
          container = Frame(self)

          container.pack(side="top", fill="both", expand=True)

          container.grid_rowconfigure(0, weight=1)
          container.grid_columnconfigure(0, weight=1)

          self.frames = {}

          for frehme in (StartPage, PageOne, PageTwo, PageThree, PageFour):
               frame = frehme(container, self)
               self.frames[frehme] = frame
               frame.grid(row=0, column=0, sticky="nsew")

          self.show_frame(StartPage)

     def show_frame(self, cont):
          
          
          frame = self.frames[cont]
          frame.tkraise()
     """

class OwnerInit():
     """
     Sets up some default values for the owner and calls CreateUser and CreateGroup to take care
     of doing that.
     """
     pass

class TablesInit():
     """
     Sets up all the tables initially with default values as needed.
     """
     #FIXME: TablesInit-Is this class needed?
     pass

class Manual():
     """
     Tk page which shows the user a table of the manual index.  User may print or view the
     entire manual or go to a chapter of the index to view or print that.  Should be recursive
     down to a particular page.
     """
     pass
