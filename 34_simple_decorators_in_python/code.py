user = {'username': 'jose', 'access_level': 'admin'}

def get_admin_password():
    return '1234'

if user.get('access_level') == 'admin':
    print(get_admin_password())    # 1234

def secure_function(func):
    if user.get('access_level') == 'admin':
        return func

get_admin_password = secure_function(get_admin_password)
print(get_admin_password())    # 1234

####################################################################################################
def make_secure(func):
    """Decorator function that checks if the user has admin permissions."""
    def secure_function():
        """Inner function that checks if the user has admin permissions."""
        if user.get('access_level') == 'admin':
            return func()
        else:
            return f"No admin permissions for {user['username']}."
    return secure_function

user = {'username': 'jose', 'access_level': 'guest'}
get_admin_password = make_secure(get_admin_password) # Decorator function
print(get_admin_password())    # No admin permissions for jose.