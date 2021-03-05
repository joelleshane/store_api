# python 2.7 from werkzeug.security import safe_str_cmp called by safe_str_cmp(user.password, password) instead of username.password == password
from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)#username_mapping.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)#userid_mapping.get(user_id, None)
