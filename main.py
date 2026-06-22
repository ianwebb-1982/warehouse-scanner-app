from purchase_order import po_list, pos_in_location
from store_location import store_locations, full_locations
from main_menu_options import main_menu
from po_menu import po_main_menu, show_purchase_order_loc
from store_loc_menu import store_loc_main_menu, loc_assign_menu
from menu_return_options import menu_return


def handle_po_menu():
    po_menu_selection = po_main_menu()
    if po_menu_selection == "1":
        for po in po_list:
            print(po)
        handle_menu_return()

    if po_menu_selection == "2":
        show_purchase_order_loc()


def handle_store_loc_menu():
    store_loc_menu_selection = store_loc_main_menu()
    if store_loc_menu_selection == "1":
        handle_loc_assign()
        handle_menu_return()
    
    if store_loc_menu_selection == "2":
        handle_view_full_locations()
        handle_menu_return()

    if store_loc_menu_selection == "3":
        handle_view_empty_locations()
        handle_menu_return()


def handle_menu_return():
    menu_return_selection = menu_return()
    if menu_return_selection == "1":
        return

    if menu_return_selection == "x":
        exit()


def handle_loc_assign():
    loc_po_to_assign: tuple = loc_assign_menu() 
    print(loc_po_to_assign[0])
    print(loc_po_to_assign[1])

    if loc_po_to_assign[0] in store_locations and loc_po_to_assign[1] in po_list:
        print("PO added to location")
        full_locations.update({loc_po_to_assign[0]: loc_po_to_assign[1]})
        po_list.remove(loc_po_to_assign[1])
        pos_in_location.append(loc_po_to_assign[1])
        store_locations.remove(loc_po_to_assign[0])
        
    """
        print(full_locations)
        print(po_list)
        print(pos_in_location)
        print(store_locations)"""


def handle_view_full_locations():
    print("--------------------")
    print("VIEW FULL LOCATIONS")
    print("--------------------")
    
    for location in full_locations:
        print(location)
    handle_menu_return()


def handle_view_empty_locations():
    print("--------------------")
    print("VIEW EMPTY LOCATIONS")
    print("--------------------")
    
    for location in store_locations:
        print(location)
    handle_menu_return()
    

def main():
    while True:
        #Main menu
        main_menu_select = main_menu()

        if main_menu_select == "1":
            handle_po_menu()

        if main_menu_select == "2":
            handle_store_loc_menu()

        if main_menu_select == "x":
            exit()


main()