from purchase_order import po_list
from warehouse_location import warehouse_locations

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


def main():
    main_menu_selection = input().lower()

    main_menu()
    po_menu()
    store_loc_menu()


    #raise exception - incorrect entry - ??? is this correct?

    
    #for location in warehouse_locations:
        #print(location)

    #for po in po_list:
        #print(po)



main()