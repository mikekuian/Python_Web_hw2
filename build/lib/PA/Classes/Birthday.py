from .Field import Field
from datetime import datetime
import re


class Birthday(Field):
    def __init__(self, birthday):
        if not self.is_valid_birthday(birthday):
            raise ValueError("Invalid birthday format (should be YYYY-MM-DD)")

        self.value = datetime.strptime(birthday, '%Y-%m-%d')

    @staticmethod
    def is_valid_birthday(birthday):
        return re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', birthday) is not None
