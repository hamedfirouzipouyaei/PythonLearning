import functools

user ={"username": "H", "access_level": "guest"}

def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return "No admin access for {}".format(user["username"])
        
    return secure_function

@make_secure
def get_admin_password():
    return "1234"

print(get_admin_password())  # Output: No admin access for H