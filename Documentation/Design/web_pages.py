#!\bin\python3
"""
Display web pages page for Wish List site.
"""

def display_web_header():
     """
     Display the start of any web page
     """
     print("""<!DOCTYPE html
     PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
     <html xmlns="http://www.w3.org/1999/xhtml" lang="en-US" xml:lang="en-US>
     """)

def display_webpage_head(page_title):
     """
     Display the <head> of each webpage
     """
     print("""<head>
     <title>""")
     print(page_title)
     print("""</title>
     <link rel="stylesheet" type="text/css" href="/css/wls_default.css" />
     <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
     </head>
     """)

def display_webpage_footer():
     """
     Display the footer for all the web pages.
     """
     print("""</html>""")

def display_admin_site_body():
     """
     Display the body of the admin site webpage
     """

def display_create_user_body():
     """"
     Display the body of the create user webpage
     """

def display_edit_user_body():
     """
     Display the body of the edit user webpage
     """

def display_user_purchases_body():
     """
     Display the body of the user purchases webpage
     """
