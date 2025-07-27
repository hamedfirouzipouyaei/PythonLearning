class User:
    def __init__(self, user_name, user_email, user_id, user_age=None):
        self.name = user_name
        self.email = user_email
        self.id = user_id
        self.age = user_age

    def year_of_birth(self, current_year):
        if self.age is not None:
            return current_year - self.age
        else:
            return None

    def is_adult(self):
        if self.age is not None:
            return self.age >= 18
        else:
            return None

