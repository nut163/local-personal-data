from src.services.ActivityService import ActivityService
from src.utils.webhook import trigger_webhook

class ActivityController:
    def __init__(self):
        self.service = ActivityService()

    def create_activity(self, activity_data):
        activity = self.service.create_activity(activity_data)
        trigger_webhook('activity_created', activity)
        return activity

    def get_activity(self, activity_id):
        activity = self.service.get_activity(activity_id)
        return activity

    def update_activity(self, activity_id, activity_data):
        activity = self.service.update_activity(activity_id, activity_data)
        trigger_webhook('activity_updated', activity)
        return activity

    def delete_activity(self, activity_id):
        self.service.delete_activity(activity_id)
        trigger_webhook('activity_deleted', activity_id)