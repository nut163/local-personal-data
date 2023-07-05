```python
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __init__(self, user_id, title, description=None):
        self.user_id = user_id
        self.title = title
        self.description = description

    def __repr__(self):
        return f"<Activity(user_id='{self.user_id}', title='{self.title}', timestamp='{self.timestamp}')>"
```