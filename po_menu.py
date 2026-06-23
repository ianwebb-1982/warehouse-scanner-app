from purchase_order import po_list
from store_location import full_locations
from menu_return_options import menu_return


def po_main_menu():
    print("PURCHASE ORDER MENU")
    print("--------------------")
    print("Menu:")
    print("1 - Show all outstanding Purchase Orders")
    print("2 - Show purchase order location")
    print("M - Return to Main Menu")
    print("--------------------")
    print("Enter your selection: ")
    po_menu_selection = input()

    return po_menu_selection
  

def show_purchase_order_loc():
    print("PURCHASE ORDER LOCATION MENU")
    print("--------------------")
    print("Enter your purchase order number: ")
    entered_po = int(float(input()))

    return entered_po

