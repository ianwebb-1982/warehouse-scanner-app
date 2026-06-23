from store_location import store_locations, full_locations
from purchase_order import po_list, pos_in_location


def store_loc_main_menu():
    print("--------------------")
    print("STORE LOCATION MENU")
    print("--------------------")
    print("Menu:")
    print("1 - Assign PO to Store Location")
    print("2 - View full locations and assigned Purchase Orders")
    print("3 - View empty Store Locations")
    print("M - Return to Main Menu")
    print("--------------------")
    print("Enter your selection: ")
    store_loc_menu_selection = input().lower()
    return store_loc_menu_selection

def loc_assign_menu_loc():
    print("--------------------")
    print("STORE LOCATIION ASSIGNMENT MENU")
    print("--------------------")
    print("Enter store location:")
    print("(e.g. - A001-B001-S001)")
    
    store_loc_to_assign = input().upper()
    return store_loc_to_assign

def loc_assign_menu_po():
    print("Enter PO number:")
    print("(e.g. - 12345)")

    po_to_assign = int(float(input()))
    return po_to_assign

def loc_assign_test_menu():
    pass










    




