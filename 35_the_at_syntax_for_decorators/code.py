import functools

user = {"username": "jose", "access_level": "guest"}


def make_secure(func):
    """Decorator function that checks if the user has admin permissions."""

    @functools.wraps(func)  # Preserves the metadata of the original function
    def secure_function():
        """Inner function that checks if the user has admin permissions."""
        if user.get("access_level") == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


@make_secure
def get_admin_password():
    return "1234"


print(get_admin_password.__name__)  # get_admin_password
print(get_admin_password())  # No admin permissions for jose.
