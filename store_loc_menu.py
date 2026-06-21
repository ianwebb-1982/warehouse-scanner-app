from store_location import store_locations, full_locations
from purchase_order import po_list, pos_in_location

def store_loc_main_menu():
    print("--------------------")
    print("STORE LOCATION MENU")
    print("--------------------")
    print("Menu:")
    print("1 - Assign PO to Store Location")
    print("2 - View full locations and assigned Purchase Orders")
    print("3 - View empty Store locations")
    print("--------------------")
    print("Enter your selection: ")
    store_loc_menu_selection()


def loc_assign_menu():
    print("--------------------")
    print("STORE LOCATIION ASSIGNMENT MENU")
    print("--------------------")
    print("Enter store location:")
    print("(e.g. - A001-B001-S001)")
    
    store_loc_to_assign = input().upper()

    print("Enter PO number:")
    print("(e.g. - 12345)")

    po_to_assign = int(float(input()))

    if store_loc_to_assign in store_locations and po_to_assign in po_list:
        print("PO added to location")
        full_locations.update({store_loc_to_assign: po_to_assign})
        po_list.remove(po_to_assign)
        pos_in_location.append(po_to_assign)
        store_locations.remove(store_loc_to_assign)
        
        '''
        print(full_locations)
        print(po_list)
        print(pos_in_location)
        print(store_locations)
        '''


def store_loc_menu_selection():
    store_loc_menu_selection = input()

    if store_loc_menu_selection == "1":
        loc_assign_menu()


    




