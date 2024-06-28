import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QMessageBox, QVBoxLayout


class ContactBookApp(QWidget):
    def __init__(self):
        super().__init__()
        self.contacts = []

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Contact Book')

        # Labels
        self.name_label = QLabel('Name:')
        self.phone_label = QLabel('Phone Number:')
        self.email_label = QLabel('Email:')
        self.address_label = QLabel('Address:')

        # Entries
        self.name_entry = QLineEdit()
        self.phone_entry = QLineEdit()
        self.email_entry = QLineEdit()
        self.address_entry = QLineEdit()

        # Buttons
        self.add_button = QPushButton('Add Contact')
        self.view_button = QPushButton('View Contacts')

        # Search functionality
        self.search_label = QLabel('Search:')
        self.search_entry = QLineEdit()
        self.search_button = QPushButton('Search')

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_entry)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_entry)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_entry)
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_entry)
        layout.addWidget(self.add_button)
        layout.addWidget(self.view_button)
        layout.addWidget(self.search_label)
        layout.addWidget(self.search_entry)
        layout.addWidget(self.search_button)

        self.setLayout(layout)

        # Connect signals to slots
        self.add_button.clicked.connect(self.add_contact)
        self.view_button.clicked.connect(self.view_contacts)
        self.search_button.clicked.connect(self.search_contact)

        self.show()

    def add_contact(self):
        name = self.name_entry.text().strip()
        phone = self.phone_entry.text().strip()
        email = self.email_entry.text().strip()
        address = self.address_entry.text().strip()

        if name and phone:  # Basic validation
            contact = {
                'name': name,
                'phone': phone,
                'email': email,
                'address': address
            }
            self.contacts.append(contact)
            QMessageBox.information(self, 'Success', 'Contact added successfully!')
            self.clear_entries()
        else:
            QMessageBox.critical(self, 'Error', 'Name and Phone Number are required fields.')

    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join(
                f"Name: {contact['name']}\nPhone: {contact['phone']}\n" for contact in
                self.contacts)
            QMessageBox.information(self, 'Contacts', contact_list)
        else:
            QMessageBox.information(self, 'Contacts', 'No contacts to display.')

    def search_contact(self):
        query = self.search_entry.text().strip().lower()
        if query:
            results = [contact for contact in self.contacts
                       if query in contact['name'].lower() or query in contact['phone']]
            if results:
                contact_list = "\n".join(
                    f"Name: {contact['name']}\nPhone: {contact['phone']}\n" for contact in results)
                QMessageBox.information(self, 'Search Results', contact_list)
            else:
                QMessageBox.information(self, 'Search Results', 'No matching contacts found.')
        else:
            QMessageBox.critical(self, 'Error', 'Please enter a search query.')

    def clear_entries(self):
        self.name_entry.clear()
        self.phone_entry.clear()
        self.email_entry.clear()
        self.address_entry.clear()
        self.search_entry.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ContactBookApp()
    sys.exit(app.exec_())
