#!/usr/bin/python3
"""
This modules holds the Tk Graphical Interface pages for the Wish List application
Some of these are the same as html pageswhile others are unique to Tk
"""

class WishListWin(Tk):
     """
     Main Window for the Tk windows for this application
     """
     pass

class SiteInitialization(Frame):
     """
     Site Initialization Window
          Site initialization needs to:
               set up databases for users, groups, calendars, wish list(s), and web site
          This page acts as an ordered checklist to accomplish these tasks
     """
     pass

class CreateUserWin(Frame):
     """
     Create a user
     """

class CreateMasterUserWin(CreateUserWin):
     """
     Create the Master Site Administrator, Site calendar and default group for Site
     """
     pass

class CreateGroupWin(Frame):
     """
     Create a new Group for the site
     """
     pass
