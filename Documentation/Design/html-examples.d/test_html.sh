#!/bin/bash

# Generate html files from jhtml files

cd calendar.d
python3 html_try.py > ../html_pages.d/calendar.html
echo "calendar generated"
cd ../shop_list_gen.d
python3 html_try.py > ../html_pages.d/shop_list_gen.html
echo "shop_list_gen generated"
cd ../user_home.d
python3 html_try.py > ../html_pages.d/user_home.html
echo "user_home generated"
cd ../user_multiple_list.d
python3 html_try.py > ../html_pages.d/user_multiple_list.html
echo "Mulitple list generated"
cd ../user_single_list.d
python3 html_try.py "Edward Birdsall" > ../html_pages.d/user_single_list-on.html
python3 html_try.py "Michael Birdsall" > ../html_pages.d/user_single_list-an.html
python3 html_try.py "Edward Birdsall" "Detail" > ../html_pages.d/user_single_list-od.html
python3 html_try.py "Michael Birdsall" "Detail"> ../html_pages.d/user_single_list-ad.html
echo "various single lists generated"
cd ../user_purch.d
python3 html_try.py > ../html_pages.d/user_purch.html
echo "user purchases generated"
cd ../user_shop.d
python3 html_try.py > ../html_pages.d/user_shop.html
echo "user shopping list"
cd ../user_edit_sug.d
python3 html_try.py adding "Edward Birdsall" > ../html_pages.d/user_edit_sug-add_oo.html
python3 html_try.py adding "Michael Birdsall" > ../html_pages.d/user_edit_sug-add_os.html
python3 html_try.py verifying "Edward Birdsall" > ../html_pages.d/user_edit_sug-ver_oo.html
python3 html_try.py verifying "Michael Birdsall" > ../html_pages.d/user_edit_sug-ver_os.html
python3 html_try.py editing "Edward Birdsall" > ../html_pages.d/user_edit_sug-edt_oo.html
python3 html_try.py editing "Michael Birdsall" > ../html_pages.d/user_edit_sug-edt_os.html
python3 html_try.py deleting "Edward Birdsall" > ../html_pages.d/user_edit_sug-del_oo.html
python3 html_try.py deleting "Michael Birdsall" > ../html_pages.d/user_edit_sug-del_os.html
cd ../user_pick_list.d
python3 html_try.py "Single" "Display"  > ../html_pages.d/user_pick_list-sd.html
python3 html_try.py "Multiple" "Display"  > ../html_pages.d/user_pick_list-md.html
python3 html_try.py "Single" "Shopping"  > ../html_pages.d/user_pick_list-ss.html
python3 html_try.py "Multiple" "Shopping"  > ../html_pages.d/user_pick_list-ms.html
echo "Various User pick list"
cd ..
echo "Done!"