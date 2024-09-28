class PasswordTooShortError(Exception):
    """Password must contain at least 8 characters"""
    pass

class PasswordTooCommonError(Exception):
    """Password must be a combination of digits, letters, and special characters"""
    pass

class PasswordNoSpecialCharactersError(Exception):
    """Password must contain at least 1 special character"""
    pass

class PasswordContainsSpacesError(Exception):
    """Password must not contain empty spaces"""
    pass

while True:
    password = input()
    if password == 'Done':
        break

    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if password.isdigit() or password.isalpha() or all(char in ["@", "*", "&", "%"] for char in password) :
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if all(char not in password for char in ["@", "*", "&", "%"]):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if ' ' in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

print("Password is valid")