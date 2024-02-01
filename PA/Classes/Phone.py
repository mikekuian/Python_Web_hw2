from .Field import Field


class Phone(Field):
    def __init__(self, number):
        if not self.is_valid_number(number):
            raise ValueError("Invalid phone number. Please enter a 10-digit number.")

        self.value = number

    @staticmethod
    def is_valid_number(number):
        return len(number) == 10 and number.isdigit()