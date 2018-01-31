#!/usr/bin/python3
"""
Display web pages page for Wish List site.
"""
class HtmlPage():
     """
     Master/Template web page class
     """
     def __init__(self):
          """
          set up pages to be a list which will be joined before sending to stdout
          """
          self.page = []

     def display_header(self, page_title="HUH"):
          """
          Display the start of any web page
          """
          self.page.append("""<!DOCTYPE html
          PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
          "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
          <html xmlns="http://www.w3.org/1999/xhtml" lang="en-US" xml:lang="en-US>
          <head>
          <title>{page_title}</title>
          <link rel="stylesheet" type="text/css" href="/css/wls_default.css" />
          <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
          </head>
          """.format(page_title=page_title))

     def display_body(self, body):
          """
          Display a default body
          """
          pass

     def display_footer(self, footer):
          """
          Display the footer for all the web pages.
          """
          self.page.append("""</html>""")

     def print_page(self):
          """
          Display the page -- print it to stdout
          joins all the parts of the page which are in a list then sends to stdout
          """
          print("".join(self.page))

class AdminPage(HtmlPage):
     """
     Body for administering a Group
     """
     def display_admin_group_body(self, page):
          """
          Display the body of the admin group webpage
          """

class AdminBSitePage(AdminPage):
     """
     Display the site administration used by the Backup Administrator
     """
     pass

class AdminMSitePage(AdminBSitePage):
     """
     Display the site Administration used by the Master Administrator
     Not sure this is needed or if this is a Tk type page depends on Master vs backup priveleges
     """

class HomePage(HtmlPage):
     """
     This displays the body of the normal user home page
     """
     def home_page(self, user, group):
          """
          Display a home page for the user
          """
          self.page[0] = display_header(self, page_title="{User Home Page")
          self.page[1] = display_user_profile(self, user)
          #FIXME: after verifying syntax for this then add all the rest of the parts of the body and footer
          self.print_page(self)

     def display_user_profile(self, user):
          """
          Shows the user profile information
          """
          pass

     def display_user_group_information(self, group):
          """
          Shows the user's group information
          if in more than one group should leave a blank line between groups
          """
          pass

     def display_user_action_buttons(self):
          """
          Display buttons for user to go to things outside this page
          """

     def display_user_wish_list(self, user_list):
          """
          Display the user's personal wish list and it's action buttons
          """
          pass

class GroupAdminHomePage(HomePage):
     """
     This displays the body of the Group Admin Home Page
     """

     def ga_home_page(self, user, group):
          """
          Display a home page for the user
          """
          self.page[0] = display_header(self, page_title="{Group Administrator Page")
          self.page[1] = display_user_profile(self, user)
          #FIXME: after verifying syntax for this then add all the rest of the parts of the body and footer
          self.print_page(self)

     def display_group_administration_buttons(self, group):
          """
          Display Group Administration buttons - goes between user buttons and personal wish list
          """
          pass

class SiteAdministratorHomePage(GroupAdminHomePage):
     """
     This displays the body of the Backup Site Administrator Home Page
     """
     pass

     def display_site_administration_buttons(self):
          """
          Display Site Administration buttons
          """

class CalendarPage(HtmlPage):
     """
     Displays a combined group and site calendar
     """

     def display_calendar():
          """
          displays the calendar
          """
          pass

     def display_user_buttons():
          """
          displays actions buttons for user
          """
          pass

     def display_group_admin_buttons():
          """"
          display action buttons for group administrator
          """"
          pass

     def display_site_admin_buttons():
          """
          display actions buttons for site administration
'''
def display_create_user_body(page):
     """"
     Display the body of the create user webpage
     """

def display_edit_user_body(page):
     """
     Display the body of the edit user webpage
     """

def display_user_purchases_body(page):
     """
     Display the body of the user purchases webpage
     """
'''