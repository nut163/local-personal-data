```python
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .db import Base

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=True)
    address = Column(String(200), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    user = relationship("User", back_populates="contacts")

    def __init__(self, user_id, name, email, phone=None, address=None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
```
