from flask import Blueprint, request
from src.controllers.ActivityController import ActivityController
from src.middleware.authentication import authenticate

activity_routes = Blueprint('activity_routes', __name__)

@activity_routes.route('/activity', methods=['POST'])
@authenticate
def create_activity():
    return ActivityController.create_activity(request.json)

@activity_routes.route('/activity/<activity_id>', methods=['GET'])
@authenticate
def get_activity(activity_id):
    return ActivityController.get_activity(activity_id)

@activity_routes.route('/activity/<activity_id>', methods=['PUT'])
@authenticate
def update_activity(activity_id):
    return ActivityController.update_activity(activity_id, request.json)

@activity_routes.route('/activity/<activity_id>', methods=['DELETE'])
@authenticate
def delete_activity(activity_id):
    return ActivityController.delete_activity(activity_id)