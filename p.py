def display_menu():
    print("\nWelcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")
    choice = input("Enter your choice (1-8): ")
    return choice

def add_contact(contacts):
    print("\nAdd New Contact")
    identifier = input("Enter phone number or email address as unique identifier: ")
    if identifier in contacts:
        print("Contact already exists.")
        return contacts
    
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address (optional): ")
    notes = input("Enter any additional notes (optional): ")

    contacts[identifier] = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address,
        'notes': notes
    }
    print("Contact added successfully.")
    return contacts

def edit_contact(contacts):
    print("\nEdit Contact")
    identifier = input("Enter the phone number or email address of the contact to edit: ")
    if identifier not in contacts:
        print("Contact not found.")
        return contacts

    contact = contacts[identifier]
    contact['name'] = input(f"Enter new name ({contact['name']}): ") or contact['name']
    contact['phone'] = input(f"Enter new phone number ({contact['phone']}): ") or contact['phone']
    contact['email'] = input(f"Enter new email address ({contact['email']}): ") or contact['email']
    contact['address'] = input(f"Enter new address ({contact['address']}): ") or contact['address']
    contact['notes'] = input(f"Enter new notes ({contact['notes']}): ") or contact['notes']
    print("Contact updated successfully.")
    return contacts

def delete_contact(contacts):
    print("\nDelete Contact")
    identifier = input("Enter the phone number or email address of the contact to delete: ")
    if identifier in contacts:
        del contacts[identifier]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")
    return contacts

def search_contact(contacts):
    print("\nSearch Contact")
    identifier = input("Enter the phone number or email address of the contact to search: ")
    contact = contacts.get(identifier)
    if contact:
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
        print(f"Notes: {contact['notes']}")
    else:
        print("Contact not found.")

def display_all_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    for identifier, contact in contacts.items():
        print(f"\nIdentifier: {identifier}")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
        print(f"Notes: {contact['notes']}")

def export_contacts(contacts, filename="contacts.txt"):
    with open(filename, 'w') as file:
        for identifier, contact in contacts.items():
            file.write(f"{identifier}\n")
            file.write(f"{contact['name']}\n")
            file.write(f"{contact['phone']}\n")
            file.write(f"{contact['email']}\n")
            file.write(f"{contact['address']}\n")
            file.write(f"{contact['notes']}\n")
            file.write("---\n")
    print(f"Contacts exported to {filename}")

def import_contacts(filename="contacts.txt"):
    contacts = {}
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                identifier = lines[i].strip()
                name = lines[i + 1].strip()
                phone = lines[i + 2].strip()
                email = lines[i + 3].strip()
                address = lines[i + 4].strip()
                notes = lines[i + 5].strip()
                contacts[identifier] = {
                    'name': name,
                    'phone': phone,
                    'email': email,
                    'address': address,
                    'notes': notes
                }
                i += 7  # Skip to the next contact block
        print(f"Contacts imported from {filename}")
    except FileNotFoundError:
        print(f"{filename} not found.")
    return contacts

def main():
    contacts = {}
    while True:
        choice = display_menu()
        if choice == '1':
            contacts = add_contact(contacts)
        elif choice == '2':
            contacts = edit_contact(contacts)
        elif choice == '3':
            contacts = delete_contact(contacts)
        elif choice == '4':
            search_contact(contacts)
        elif choice == '5':
            display_all_contacts(contacts)
        elif choice == '6':
            export_contacts(contacts)
        elif choice == '7':
            contacts = import_contacts()
        elif choice == '8':
            print("Exiting the Contact Management System.")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 8.")


main()
