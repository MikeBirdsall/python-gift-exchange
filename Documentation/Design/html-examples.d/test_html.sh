#!/bin/bash

# Generate html files from jhtml files

cd calendar.d
python3 html_try.py > ../html_pages.d/calendar.html
cd ../shop_list_gen.d
python3 html_try.py > ../html_pages.d/shop_list_gen.html
cd ../user_home.d
python3 html_try.py > ../html_pages.d/user_home.html
cd ../user_multiple_list.d
python3 html_try.py > ../html_pages.d/user_multiple_list.html
cd ../user_single_list.d
python3 html_try.py > ../html_pages.d/user_single_list.html
cd ../user_purch.d
python3 html_try.py > ../html_pages.d/user_purch.html
cd ../user_shop.d
python3 html_try.py > ../html_pages.d/user_shop.html
cd ../user_edit_sug.d
python3 html_try.py adding "Edward Birdsall" > ../html_pages.d/user_edit_sug-add_oo.html
python3 html_try.py adding "Michael Birdsall" > ../html_pages.d/user_edit_sug-add_os.html
python3 html_try.py verifying "Edward Birdsall" > ../html_pages.d/user_edit_sug-ver_oo.html
python3 html_try.py verifying "Michael Birdsall" > ../html_pages.d/user_edit_sug-ver_os.html
python3 html_try.py editing "Edward Birdsall" > ../html_pages.d/user_edit_sug-edt_oo.html
python3 html_try.py editing "Michael Birdsall" > ../html_pages.d/user_edit_sug-edt_os.html
python3 html_try.py deleting "Edward Birdsall" > ../html_pages.d/user_edit_sug-del_oo.html
python3 html_try.py deleting "Michael Birdsall" > ../html_pages.d/user_edit_sug-del_os.html
cd ..
#user pick list
# single display
#multiple display
#single shopping list
# multiple shopping list