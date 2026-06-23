from purchase_order import po_list, pos_in_location
from store_location import store_locations, full_locations
from main_menu_options import main_menu
from po_menu import po_main_menu, show_purchase_order_loc
from store_loc_menu import store_loc_main_menu, loc_assign_menu_loc, loc_assign_menu_po
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
    elif po_menu_selection == "2":
        handle_show_full_locations()
        handle_menu_return()
    elif po_menu_selection == "m":
        return
    else:
        clear_screen()
        print("Enter Correct Choice")
        handle_po_menu()



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
        print(f"Purchase Order {full_po} is in location {keys}")


######
# Store location menus
def handle_store_loc_menu():
    store_loc_menu_selection = store_loc_main_menu()
    if store_loc_menu_selection == "1":
        handle_loc_assign()
        handle_menu_return()
    elif store_loc_menu_selection == "2":
        handle_view_full_locations()
        handle_menu_return()
    elif store_loc_menu_selection == "3":
        handle_view_empty_locations()
        handle_menu_return()
    elif store_loc_menu_selection == "m":
        return
    else:
        clear_screen()
        print("Enter Correct Choice")
        handle_store_loc_menu()

# Store location option 1
def handle_loc_assign():
    clear_screen()
    assign_loc = loc_assign_menu_loc() 
    
  
    if assign_loc in store_locations:
        loc_to_assign = assign_loc
        store_locations.remove(loc_to_assign)
    else:
        clear_screen()
        print("Enter correct Store Location")
        handle_loc_assign()

    assign_po = loc_assign_menu_po()

    if assign_po in po_list:
        po_to_assign = assign_po
        po_list.remove(po_to_assign)
        pos_in_location.append(po_to_assign)
    else:
        clear_screen()
        print("Enter correct Purchase Order")
        #handle_loc_assign()
        handle_loc_assign()

    full_locations.update({loc_to_assign: po_to_assign})
 

# Store location option 2
def handle_view_full_locations():
    clear_screen()
    print("--------------------")
    print("VIEW FULL LOCATIONS")
    print("--------------------")

    for key, val in full_locations.items():
        print(f"Location {key}: Order {val}")

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
        elif main_menu_select == "2":
            clear_screen()
            handle_store_loc_menu()
        elif main_menu_select == "x":
            exit()
        else:
            clear_screen()
            print("Enter Correct Choice")

main()