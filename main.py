from purchase_order import po_list, pos_in_location
from store_location import store_locations, full_locations
from main_menu_options import main_menu
from po_menu import po_main_menu, show_purchase_order_loc
from store_loc_menu import store_loc_main_menu, loc_assign_menu
from menu_return_options import menu_return
import os

#######
# Menu return logic
def handle_menu_return():
    menu_return_selection = menu_return()
    if menu_return_selection == "1":
        return

    if menu_return_selection == "x":
        exit()

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#######
# PO Menus
def handle_po_menu():
    po_menu_selection = po_main_menu()
    if po_menu_selection == "1":
        handle_show_pos()

    if po_menu_selection == "2":
        handle_show_full_locations()
        handle_menu_return()

def handle_show_pos():
        clear_screen()
        print("---------------")
        print("Available Purchase Orders")
        print("---------------")

        for po in po_list:
            print(po)
        handle_menu_return()

def handle_show_full_locations():
    clear_screen()
    full_po = show_purchase_order_loc()

    if full_po in full_locations.values():

        keys = [key for key, val in full_locations.items() if val == full_po]
        print(keys)


######
# Store location menus
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

# Store location option 1
def handle_loc_assign():
    clear_screen()
    loc_po_to_assign: tuple = loc_assign_menu() 
    #print(loc_po_to_assign[0]) #Test print
    #print(loc_po_to_assign[1]) #test print

    if loc_po_to_assign[0] in store_locations and loc_po_to_assign[1] in po_list:
        print("PO added to location")
        full_locations.update({loc_po_to_assign[0]: loc_po_to_assign[1]})
        po_list.remove(loc_po_to_assign[1])
        pos_in_location.append(loc_po_to_assign[1])
        store_locations.remove(loc_po_to_assign[0])
        
# Store location option 2
def handle_view_full_locations():
    clear_screen()
    print("--------------------")
    print("VIEW FULL LOCATIONS")
    print("--------------------")
    
    for location in full_locations:
        for order in full_locations.values():
            print(f"Location {location}: Order {order}")

# Store location option 3
def handle_view_empty_locations():
    clear_screen()
    print("--------------------")
    print("VIEW EMPTY LOCATIONS")
    print("--------------------")

    for location in store_locations:
        print(location)
  
    
######
def main():
    while True:
        #Main menu
        clear_screen()
        main_menu_select = main_menu()

        if main_menu_select == "1":
            clear_screen()
            handle_po_menu()

        if main_menu_select == "2":
            clear_screen()
            handle_store_loc_menu()

        if main_menu_select == "x":
            exit()


main()