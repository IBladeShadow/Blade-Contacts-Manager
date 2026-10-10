import json
from colorama import Fore, Style
import pyfiglet
import os 
with open("contacts.json", "r", encoding="utf-8") as f:
    data = json.load(f)
contacts = data["contacts"]
numbers = data["numbers"]
def save_contacts():
    with open("contacts.json", "w", encoding="utf-8") as f:
        json.dump(
            {
             "contacts": contacts,
             "numbers": numbers
             },
            f,
            ensure_ascii=False,
            indent=4
        )

def add_contact():
    while True:
        name = input("Enter Name: ")
        if name in contacts:
            print("This contact already exists!")
            continue
        contacts.append(name) 
        number = input("Enter Number: ")
        if len(number) == 11 :
            numbers.append(number)
            save_contacts()
            break
        else:
            print("Please Enter Correct Number!")
            continue
    

def show_contacts():
    try:
        if not contacts:
            print("No contacts found")
            return
        for index, name in enumerate(contacts):
                print(f"{index}. {name} {numbers[index]}")
    except IndexError:print(Fore.RED + "Erorr List Damaged!" + Style.RESET_ALL)
    input("Press Enter to continue...")

def search_contact():
        raw = input("Search Your Contacts: ")
        found = [index for index, name in enumerate(contacts)
                if raw.lower() in name.lower()]
        if found:
            for index in found:
                print(f"{index}. {contacts[index]} - {numbers[index]}")
        else:
            print("Contact not found")
        input("Press Enter to continue...")    

def delete_contact():
    raw = input("Delete Contact: ")
    found = [index for index, name in enumerate(contacts)
                if raw in name]
    if not found:
        print("Contact not found")
        return
    if found:
        for index in found:
            print(f"{index}. {contacts[index]} - {numbers[index]}")
        while True:
            choise = input("Are You Sure?(n/y)")
            if choise == "y":
                index = found[0]
                contacts.pop(index)
                numbers.pop(index)
                save_contacts()
                print("Contact deleted")
                input("Press Enter to continue...")
                break
            elif choise == "n":
                input("Press Enter to continue...")
                break
            else:
                print("Press N or Y")
                continue


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
                break

            else:
                print("Please Choose 1-5")
    except KeyboardInterrupt:
        print("")
    finally:
        print(Fore.WHITE + "Good Bye" + Style.RESET_ALL)

main()