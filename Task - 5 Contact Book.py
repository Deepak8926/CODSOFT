contacts = []

while True:
    print("\nContact Manager")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts.append({"name": name, "phone": phone})
        print(f"Contact {name} added.")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            for contact in contacts:
                print(f"Name: {contact['name']}, phone: {contact['phone']}")

    elif choice == "3":
        search_name = input("Enter the name to search: ")
        found = False
        for contact in contacts:
            if search_name.lower() in contact['name'].lower():
                print(f"Found: Name:{contact['name'], phone: {contact['phone']}}")
                found = True
        if not found:
            print("Contact not found.")

    elif choice == "4":
        search_name = input("Enter the name of contact to be updated. ")
        found = False
        for contact in contacts:
            if search_name.lower() in contact['name'].lower():
                new_phone = input(f"Enter new phone number for {contact['name']}: ")
                contact['phone'] = new_phone
                print(f"{contact['name']}'s phone number updated.")
                found = True
        if not found:
            print("Contact not found.")

    elif choice == "5":
        search_name = input("Enter the name of the contact to delete: ")
        found = False
        for contact in contacts:
            if search_name.lower()in contact['name'].lower():
                contacts.remove(contact)
                print(f"Contact {contact['name']} deleted.")
                found = True
        if not found:
            print("Contact not found.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option,choose between 1 and 6.")                                







