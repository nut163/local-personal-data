```python
from src.models.Contact import Contact
from src.database.contactQueries import ContactQueries

class ContactService:
    def __init__(self):
        self.contact_queries = ContactQueries()

    def create_contact(self, contact_data):
        new_contact = Contact(**contact_data)
        return self.contact_queries.insert_contact(new_contact)

    def get_contact(self, contact_id):
        return self.contact_queries.select_contact_by_id(contact_id)

    def update_contact(self, contact_id, updated_data):
        return self.contact_queries.update_contact_by_id(contact_id, updated_data)

    def delete_contact(self, contact_id):
        return self.contact_queries.delete_contact_by_id(contact_id)

    def get_all_contacts(self):
        return self.contact_queries.select_all_contacts()
```