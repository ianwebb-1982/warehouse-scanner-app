from po_menu import po_main_menu
from store_loc_menu import store_loc_main_menu

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
    return main_menu_select

    '''
    if main_menu_select != "1" or main_menu_select != "2":
        print("Incorrect number entered.")
        main_menu()
    '''

