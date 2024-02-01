from .Field import Field
import re


class Email(Field):
    def __init__(self, email):
        if not self.is_valid_email(email):
            raise ValueError("Invalid email format")

        self.value = email

    @staticmethod
    def is_valid_email(email):
        return re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)