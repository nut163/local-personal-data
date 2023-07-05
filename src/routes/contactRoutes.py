from flask import Blueprint, request
from src.controllers.ContactController import ContactController
from src.middleware.authentication import authenticate

contact_routes = Blueprint('contact_routes', __name__)

@contact_routes.route('/contacts', methods=['GET'])
@authenticate
def get_contacts():
    return ContactController.get_all_contacts()

@contact_routes.route('/contacts/<contact_id>', methods=['GET'])
@authenticate
def get_contact(contact_id):
    return ContactController.get_contact(contact_id)

@contact_routes.route('/contacts', methods=['POST'])
@authenticate
def create_contact():
    return ContactController.create_contact(request.get_json())

@contact_routes.route('/contacts/<contact_id>', methods=['PUT'])
@authenticate
def update_contact(contact_id):
    return ContactController.update_contact(contact_id, request.get_json())

@contact_routes.route('/contacts/<contact_id>', methods=['DELETE'])
@authenticate
def delete_contact(contact_id):
    return ContactController.delete_contact(contact_id)