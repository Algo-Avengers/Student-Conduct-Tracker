from App.models import staff
from App.database import db

def create_user(username, password):
    newuser = staff(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return staff.query.filter_by(username=username).first()

def get_user(id):
    return staff.query.get(id)

def get_all_users():
    return staff.query.all()

def get_all_users_json():
    users = staff.query.all()
    if not users:
        return []
    users = [staff.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None

def toJSON(user):
    if user:
        return {
            "id": user.id,
            "username": user.username,
            "authorized": user.is_authorized()
        }
    return None