# models.py

#from app.orm import ORM

class User(ORM):
    _table = 'users'
    _columns = ['id', 'username', 'email', 'password_hash']

    def __init__(self, username, email, password_hash, id=None):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash

    def add_meal(self, meal_name, description, calories):
        # method to add a meal for this user
        pass

    def delete_meal(self, meal_id):
        # method to delete a meal for this user
        pass

    def view_meals(self):
        # method to view meals for this user
        pass

    def suggest_meal(self):
        #method to suggest a meal based on user preferences
        pass