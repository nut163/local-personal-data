```python
from src.models.Activity import Activity
from src.database.activityQueries import ActivityQueries

class ActivityService:
    def __init__(self):
        self.activity_queries = ActivityQueries()

    def create_activity(self, activity_data):
        activity = Activity(**activity_data)
        return self.activity_queries.create_activity(activity)

    def get_activity(self, activity_id):
        return self.activity_queries.get_activity(activity_id)

    def update_activity(self, activity_id, activity_data):
        return self.activity_queries.update_activity(activity_id, activity_data)

    def delete_activity(self, activity_id):
        return self.activity_queries.delete_activity(activity_id)

    def get_all_activities(self):
        return self.activity_queries.get_all_activities()
```