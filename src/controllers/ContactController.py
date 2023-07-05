```python
from flask import request, jsonify
from src.services.ContactService import ContactService
from src.utils.webhook import trigger_webhook

class ContactController:

    @staticmethod
    def get_all_contacts():
        contacts = ContactService.get_all_contacts()
        return jsonify({'contacts': contacts}), 200

    @staticmethod
    def get_contact_by_id(contact_id):
        contact = ContactService.get_contact_by_id(contact_id)
        if contact:
            return jsonify({'contact': contact}), 200
        else:
            return jsonify({'error': 'Contact not found'}), 404

    @staticmethod
    def create_contact():
        data = request.get_json()
        new_contact = ContactService.create_contact(data)
        trigger_webhook('contact_created', new_contact)
        return jsonify({'contact': new_contact}), 201

    @staticmethod
    def update_contact(contact_id):
        data = request.get_json()
        updated_contact = ContactService.update_contact(contact_id, data)
        if updated_contact:
            trigger_webhook('contact_updated', updated_contact)
            return jsonify({'contact': updated_contact}), 200
        else:
            return jsonify({'error': 'Contact not found'}), 404

    @staticmethod
    def delete_contact(contact_id):
        deleted = ContactService.delete_contact(contact_id)
        if deleted:
            trigger_webhook('contact_deleted', contact_id)
            return jsonify({'message': 'Contact deleted'}), 200
        else:
            return jsonify({'error': 'Contact not found'}), 404
```