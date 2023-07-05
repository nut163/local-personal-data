```python
from src.models.User import User
from src.database.db import db

def get_user_by_id(user_id):
    return db.session.query(User).filter(User.id == user_id).first()

def get_user_by_email(email):
    return db.session.query(User).filter(User.email == email).first()

def create_user(user_data):
    new_user = User(**user_data)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def update_user(user_id, user_data):
    user = get_user_by_id(user_id)
    if user:
        for key, value in user_data.items():
            setattr(user, key, value)
        db.session.commit()
    return user

def delete_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return user
```