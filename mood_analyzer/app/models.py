from . import mongo

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        users_collection = mongo.db.users
        users_collection.insert_one({'username': self.username, 'password': self.password})
