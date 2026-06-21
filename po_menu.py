from purchase_order import po_list
from store_location import full_locations


def po_main_menu():
    print("PURCHASE ORDER MENU")
    print("--------------------")
    print("Menu:")
    print("1 - Show all outstanding Purchase Orders")
    print("2 - Show purchase order location")
    print("--------------------")
    print("Enter your selection: ")
    po_menu_selection()


def po_menu_selection():
    po_menu_selection = input()

    if po_menu_selection == "1":
        for po in po_list:
            print(po)

    if po_menu_selection == "2":
        show_purchase_order_loc()

def show_purchase_order_loc():
    '''
    mydict = {'george': 16, 'amber': 19}
    print(list(mydict.keys())[list(mydict.values()).index(16)])  # Prints george
    '''
    entered_po = input()

    print(list(full_locations.keys())[list(full_locations()).index(entered_po)])