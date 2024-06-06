# lib/cli.py

from helpers import (
    exit_program,
    list_stylists,
    find_stylist_by_name,
    find_stylist_by_id,
    create_stylist,
    update_stylist,
    delete_stylist,
    list_clients,
    find_client_by_name,
    find_client_by_id,
    create_client,
    update_client,
    delete_client,
    list_stylist_clients,
)
def previous_menu():
    main()

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            stylist_choices()
        elif choice == "2":
            client_choices()
    

def stylist_choices():
    while True:
        stylist_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_stylists()
        elif choice == "2":
            find_stylist_by_name()
        elif choice == "3":
            find_stylist_by_id()
        elif choice == "4":
            create_stylist()
        elif choice == "5":
            update_stylist()
        elif choice == "6":
            delete_stylist()
        elif choice == "7":
            list_stylist_clients()
        elif choice == "8":
            previous_menu()
        else:
            print("Invalid choice")
        
def client_choices():
    while True:
        client_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_clients()
        elif choice == "2":
            find_client_by_name()
        elif choice == "3":
            find_client_by_id()
        elif choice == "4":
            create_client()
        elif choice == "5":
            update_client()
        elif choice == "6":
            delete_client()
        elif choice == "7":
            list_stylist_clients()
        elif choice == "8":
            previous_menu()
        else:
            print("Invalid choice")
        

def menu():
    print()
    print("The Salon")
    print()
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Stylist Menu")
    print("2. Client Menu")

def stylist_menu():
    print()
    print("Please select an option:")
    print("1. List all stylists")
    print("2. Find stylist by name")
    print("3. Find stylist by id")
    print("4: Create stylist")
    print("5: Update stylist")
    print("6: Delete stylist")
    print("7: List all clients for a stylist")
    print("8: Main menu")

def client_menu():
    print()
    print("Please select an option:")
    print("1. List all clients")
    print("2. Find client by name")
    print("3. Find client by id")
    print("4: Create client")
    print("5: Update client")
    print("6: Delete client")
    print("7: List all clients for a stylist")
    print("8: Main menu")


if __name__ == "__main__":
    main()
