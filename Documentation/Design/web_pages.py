#!\bin\python3
"""
Display web pages page for Wish List site.
"""
class HtmlPage():
     """
     """
     def __init__(self):
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
          pass

     def display_footer(self, footer):
          """
          Display the footer for all the web pages.
          """
          self.page.append("""</html>""")

     def print_page(self):
          print("".join(self.page))

class AdminPage(HtmlPage):
     def display_admin_site_body(self, page):
          """
          Display the body of the admin site webpage
          """

class HomePage(HtmlPage):
     pass





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