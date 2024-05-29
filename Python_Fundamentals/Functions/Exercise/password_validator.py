def check_validity(input_string):
    password_status = []

    def check_length(input_string):
        if not 6 <= len(input_string) <= 10:
            password_status.append("Password must be between 6 and 10 characters")

    def check_chars(input_string):
        if not input_string.isalnum():
            password_status.append("Password must consist only of letters and digits")

    def check_digits(input_string):
        digits = 0
        for char in input_string:
            if char.isdigit():
                digits += 1
        if digits < 2:
            password_status.append("Password must have at least 2 digits")

        return True
    check_length(input_string)
    check_chars(input_string)
    check_digits(input_string)

    if len(password_status) == 0:
        print("Password is valid")
    else:
        for error in password_status:
            print(error)


input_string = input()
check_validity(input_string)
