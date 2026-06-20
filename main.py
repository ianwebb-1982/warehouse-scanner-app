from purchase_order import po_list
from warehouse_location import warehouse_locations

main_menu_select = 0


def main_menu():
    print("WAREHOUSE MANAGEMENT APP")
    print("--------------------")
    print("Menu:")
    print("1 - Purchase Orders")
    print("2 - Store Locations")
    print("--------------------")
    print("Enter your selection: ")

def po_menu():
    print("PURCHASE ORDER MENU")
    print("--------------------")
    print("Menu:")
    print("1 - Show all Purchase Orders")
    print("2 - Show outstanding Purchase Orders")
    print("3 - Show purchase order location")
    print("--------------------")
    print("Enter your selection: ")

def store_loc_menu():
    print("STORE LOCATION MENU")
    print("--------------------")
    print("Menu:")
    print("1 - Assign PO to Store Location")
    print("2 - View full locations and assigned Purchase Orders")
    print("3 - View empty Store locations")
    print("--------------------")
    print("Enter your selection: ")

def menu_selection():
    main_menu_selection = input()
    
    if main_menu_selection != "1" or main_menu_selection != "2":
        print("Incorrect number entered.")
        main_menu()

    if main_menu_selection == "1":
        po_menu()
        po_menu_selection= input()

    if main_menu_selection == "2":
        store_loc_menu()
        store_loc_menu_selection = input()


def main():


    main_menu()
    menu_selection()
    

    
    #for location in warehouse_locations:
        #print(location)

    #for po in po_list:
        #print(po)
    


main()