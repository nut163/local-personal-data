```python
from src.models.Contact import Contact
from src.database.db import db

def get_all_contacts():
    return db.session.query(Contact).all()

def get_contact_by_id(id):
    return db.session.query(Contact).filter(Contact.id == id).first()

def create_contact(data):
    new_contact = Contact(**data)
    db.session.add(new_contact)
    db.session.commit()
    return new_contact

def update_contact(id, data):
    contact = db.session.query(Contact).filter(Contact.id == id).first()
    if contact:
        for key, value in data.items():
            setattr(contact, key, value)
        db.session.commit()
        return contact
    return None

def delete_contact(id):
    contact = db.session.query(Contact).filter(Contact.id == id).first()
    if contact:
        db.session.delete(contact)
        db.session.commit()
        return True
    return False
```