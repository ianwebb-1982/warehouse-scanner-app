from purchase_order import po_list
from store_location import store_locations
from main_menu_options import main_menu
from po_menu import po_main_menu, show_purchase_order_loc
from store_loc_menu import store_loc_main_menu, loc_assign_menu, view_full_locations, view_empty_locations

def handle_po_menu():
    po_menu_selection = po_main_menu()
    if po_menu_selection == "1":
        for po in po_list:
            print(po)

    if po_menu_selection == "2":
        show_purchase_order_loc()


def handle_store_loc_menu():
    store_loc_menu_selection = store_loc_main_menu()
    if store_loc_menu_selection == "1":
        loc_assign_menu()
    
    if store_loc_menu_selection == "2":
        view_full_locations()

    if store_loc_menu_selection == "3":
        view_empty_locations()

def main():

    #Main menu
    main_menu_select = main_menu()

    if main_menu_select == "1":
        handle_po_menu()

    if main_menu_select == "2":
        handle_store_loc_menu()


main()