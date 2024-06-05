# lib/helpers.py
from models.client import Client
from models.stylist import Stylist

def exit_program():
    print()
    print("See you next time!")
    exit()

def list_stylists():
    stylists = Stylist.get_all()
    for stylist in stylists:
        print(stylist)

def find_stylist_by_name():
    name = input("Enter a stylist's name: ")
    stylist = Stylist.find_by_name(name)
    print(stylist) if stylist else print(f"Stylist {name} not found")


def find_stylist_by_id():
    id = input("Enter the stylist's id: ")
    stylist = Stylist.find_by_id(id)
    print(stylist) if stylist else print(f"Stylist {id} not found")

def create_stylist():
    name = input("Enter stylist's name: ")
    specialization = input("Enter stylist's specialization: ")
    years_worked = input("Enter stylist's years worked: ")
    try:
        stylist = Stylist.create(name, specialization, years_worked)
        print(f"Success: {stylist}")
    except Exception as exc:
        print("Error creating stylist: ", exc)

def update_stylist():
    id_ = input("Enter the stylist's id: ")
    if stylist := Stylist.find_by_id(id_):
        try:
            name = input("Enter stylist's name: ")
            stylist.name = name
            specialization = input("Enter stylist's specialization: ")
            stylist.specialization = specialization
            years_worked = input("Enter stylist's years worked: ")
            stylist.years_worked = years_worked

            stylist.update()
            print(f"Success: {stylist}")
        except Exception as exc:
            print("Error updating stylist: ", exc)
    else:   
        print(f"Stylist {id_} not found")

def delete_stylist():
    id_ = input("Enter the stylist's id: ")
    if stylist := Stylist.find_by_id(id_):
        stylist.delete()
        print(f"Success: {stylist} deleted")
    else:   
        print(f"Stylist {id_} not found")    

def list_clients():
    clients = Client.get_all()
    for client in clients:
        print(client)

def find_client_by_name():
    name = input("Enter a client's name: ")
    client = Client.find_by_name(name)
    print(client) if client else print(f"Client {name} not found")

def find_client_by_id():
    id = input("Enter the client's id: ")
    client = Client.find_by_id(id)
    print(client) if client else print(f"Client {id} not found")

def create_client():
    name = input("Enter client's name: ")
    phone_number = input("Enter client's phone number: ")
    email = input("Enter client's email: ")
    stylist_id = input("Enter client's stylist id: ")
    try:
        client = Client.create(name, phone_number, email, stylist_id)
        print(f"Success: {client}")
    except Exception as exc:
        print("Error creating client: ", exc)

def update_client():
    id_ = input("Enter the client's id: ")
    if client := Client.find_by_id(id_):
        try:
            name = input("Enter client's name: ")
            client.name = name
            phone_number = input("Enter client's phone number: ")
            client.phone_number = phone_number
            email = input("Enter client's email: ")
            client.email = email
            stylist_id = input("Enter client's stylist id: ")
            client.stylist_id = stylist_id

            client.update()
            print(f"Success: {client}")
        except Exception as exc:
            print("Error updating client: ", exc)

def delete_client():
    id_ = input("Enter the client's id: ")
    if client := Client.find_by_id(id_):
        client.delete()
        print(f"Success: {client} deleted")
    else:   
        print(f"Client {id_} not found")

def list_stylist_clients():
    id_ = input("Enter the stylist's id: ")
    if stylist := Stylist.find_by_id(id_):
        clients = stylist.get_clients()
        for client in clients:
            print(client)
    else:
        print(f"Stylist {id_} not found")
