from purchase_order import po_list
from store_location import store_locations
from main_menu_options import main_menu, main_menu_selection
from


def main():

    main_menu()
    main_menu_selection()

    if main_menu_select == "1":
        po_main_menu()

    if main_menu_select == "2":
        store_loc_main_menu()
   
   
main()