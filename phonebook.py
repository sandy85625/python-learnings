
"""
Create a Class for menu driven program to implement phone using dictionary. It implements functions:
 - add_contact
 - find_contact
 - list_contact

"""
class Phonebook:
    def __init__(self):
        self.phonebook = {}
    
    def add_contact(self):
        name = input("\nEnter contact name: ")
        number = input("Enter contact number: ")
        self.phonebook[name] = number
        print(f"\nAdded {name} with number {number} to phonebook")

    def find_contact(self):
        name = input("\nEnter contact name: ")
        if name in self.phonebook:
            print(f"{name}: {self.phonebook[name]}")
        else:
            print(f"{name} not found in phonebook")

    def list_contacts(self):
        print("\nContacts in phonebook:")
        for name, number in self.phonebook.items():
            print(f"{name}: {number}")
            

phonebook = Phonebook()

while True:
    print("===========================================")
    print("\nPhonebook Menu:")
    print("\n1. Add Contact")
    print("2. Find Contact")
    print("3. List Contacts")
    print("4. Quit")
    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        phonebook.add_contact()
    elif choice == "2":
        phonebook.find_contact()
    elif choice == "3":
        phonebook.list_contacts()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
