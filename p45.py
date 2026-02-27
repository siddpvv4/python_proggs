#Contact Book (Menu-Driven Dictionary)
contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Store Contact\n2. Search Contact\n3. Update Contact\n4. Delete Contact\n5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact saved successfully.")
        
    elif choice == '2':
        name = input("Enter name to search: ")
        # .get() prevents KeyError if the name doesn't exist
        print(f"Phone Number: {contacts.get(name, 'Contact not found.')}")
        
    elif choice == '3':
        name = input("Enter name to update: ")
        if name in contacts:
            new_phone = input("Enter new phone number: ")
            contacts[name] = new_phone
            print("Contact updated.")
        else:
            print("Contact not found.")
            
    elif choice == '4':
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")
            
    elif choice == '5':
        print("Exiting Contact Book.")
        break
        
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")