import re


class Validator:
    @classmethod
    def is_valid_email(cls, email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return True if re.match(email_regex, email) else False


print(Validator.is_valid_email("test@example.com"))
print(Validator.is_valid_email("invalid-email"))
