import json
from colorama import Fore, Style
import pyfiglet
import os 
with open("contacts.json", "r", encoding="utf-8") as f:
    data = json.load(f)
contacts = data["contacts"]

def save_contacts():
    with open("contacts.json", "w", encoding="utf-8") as f:
        json.dump(
            {"contacts": contacts},
            f,
            ensure_ascii=False,
            indent=4
        )

def add_contact():
    name = input("Enter Name: ")
    contacts.append(name)
    save_contacts()

def show_contacts():
    if not contacts:
        print("No contacts found")
        return
    for index, name in enumerate(contacts):
        print(f"{index}. {name}")
    input("Press Enter to continue...")

def search_contact():
    raw = input("Search Your Contacts: ")
    found = [name for name in contacts if raw.lower() in name.lower()]
    if found:
        for name in found:
            print(name)
    else:
        print("Contact not found")

def delete_contact():
    raw = input("Delete Contact: ")
    found = [name for name in contacts if raw.lower() in name.lower()]
    if not found:
        print("Contact not found")
        return
    for name in found:
        contacts.remove(name)
    save_contacts()
    print("Contact deleted")


def main():
    os.system("cls")
    try:
        while True:
            print(
                Fore.LIGHTBLUE_EX
                + pyfiglet.figlet_format("------------------------------\n  Blade Contacts Manager\n------------------------------", font="mini")
                + Style.RESET_ALL
            )
            print(Fore.GREEN + "1. Add Contact")
            print("2. Show Contacts")
            print("3. Search Contact")
            print(Fore.RED + "4. Delete Contact")
            print("5. Exit" + Style.RESET_ALL)

            raw = input(Fore.LIGHTYELLOW_EX + "Choose: "+ Style.RESET_ALL)

            if not raw.isdigit():
                print("Please Choose 1-5")
                continue

            choice = int(raw)

            if choice == 1:
                add_contact()

            elif choice == 2:
                show_contacts()

            elif choice == 3:
                search_contact()

            elif choice == 4:
                delete_contact()

            elif choice == 5:
                print(Fore.WHITE + "Good Bye" + Style.RESET_ALL)
                break

            else:
                print("Please Choose 1-5")
    except KeyboardInterrupt:
        print("")
    finally:
        print(Fore.WHITE + "Good Bye" + Style.RESET_ALL)

main()

