from .Field import Field


class Name(Field):
    def __init__(self, name):
        if not self.is_valid_name(name):
            raise ValueError("Invalid name. Please enter at least 2 characters")

        self.value = name

    @staticmethod
    def is_valid_name(name):
        return len(name) > 1
