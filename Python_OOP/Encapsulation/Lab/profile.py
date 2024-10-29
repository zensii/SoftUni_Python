import re

class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__username

    @username.setter
    def username(self, user_name):
        if 5 <= len(user_name) <= 15:
            self.__username = user_name
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @password.setter
    def password(self, pass_word):
        pat_d = r'[0-9]'
        pat_l = r'[A-Z]'
        digit_present = re.findall(pat_d, pass_word)
        upper_l_present = re.findall(pat_l, pass_word)
        if 8 <= len(pass_word) and digit_present and upper_l_present:
            self.__password = pass_word
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")


    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
