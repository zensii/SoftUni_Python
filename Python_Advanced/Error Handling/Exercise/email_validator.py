class NameTooShortError(Exception):
    """Name must be more than 4 characters"""
    pass

class MustContainAtSymbolError(Exception):
    """Email must contain @"""
    pass

class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""
    pass

while True:
    email = input()
    if email == 'End':
        break

    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name = email.split('@')[0]
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if '.' not in email or email.split('.')[-1] not in ['com', 'bg', 'org', 'net']:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
