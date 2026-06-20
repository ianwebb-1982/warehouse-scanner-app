from po_menu import po_main_menu
from store_loc_menu import store_loc_main_menu, store_loc_menu_selection

def main_menu():
    print("WAREHOUSE MANAGEMENT APP")
    print("--------------------")
    print("Menu:")
    print("1 - Purchase Orders")
    print("2 - Store Locations")
    print("--------------------")
    print("Enter your selection: ")


def main_menu_selection():
    main_menu_select = input()
    
    if main_menu_selection != "1" or main_menu_selection != "2":
        print("Incorrect number entered.")
        main_menu()

    if main_menu_selection == "1":
        po_main_menu()
        po_menu_selection= input()

    if main_menu_selection == "2":
        store_loc_main_menu()
        store_loc_menu_selection = input()