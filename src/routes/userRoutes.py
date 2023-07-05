from flask import Blueprint, request
from src.controllers.UserController import UserController
from src.middleware.authentication import auth_required

userRoutes = Blueprint('userRoutes', __name__)

userController = UserController()

@userRoutes.route('/users', methods=['GET'])
@auth_required
def get_users():
    return userController.get_users()

@userRoutes.route('/users/<id>', methods=['GET'])
@auth_required
def get_user(id):
    return userController.get_user(id)

@userRoutes.route('/users', methods=['POST'])
@auth_required
def create_user():
    data = request.get_json()
    return userController.create_user(data)

@userRoutes.route('/users/<id>', methods=['PUT'])
@auth_required
def update_user(id):
    data = request.get_json()
    return userController.update_user(id, data)

@userRoutes.route('/users/<id>', methods=['DELETE'])
@auth_required
def delete_user(id):
    return userController.delete_user(id)