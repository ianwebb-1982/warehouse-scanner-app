from purchase_order import po_list

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
        for po 