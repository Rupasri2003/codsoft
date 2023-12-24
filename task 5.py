class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}

    def view_all_contacts(self):
        for name, details in self.contacts.items():
            print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")

    def search_contact(self, keyword):
        for name, details in self.contacts.items():
            if keyword.lower() in name.lower() or keyword in details['Phone']:
                print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")

    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
        if name in self.contacts:
            contact = self.contacts[name]
            if new_phone:
                contact['Phone'] = new_phone
            if new_email:
                contact['Email'] = new_email
            if new_address:
                contact['Address'] = new_address
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

# Example usage
contact_book = ContactBook()

contact_book.add_contact('John Doe', '123-456-7890', 'john@example.com', 'ooty')
contact_book.add_contact('Jane Smith', '987-654-3210', 'jane@example.com', 'goa')

contact_book.view_all_contacts()

contact_book.search_contact('John')

contact_book.update_contact('John Doe', new_phone='999-888-7777', new_email='newjohn@example.com')
contact_book.view_all_contacts()

contact_book.delete_contact('Jane Smith')
contact_book.view_all_contacts()
