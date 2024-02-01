from .Name import Name
from .Phone import Phone
from .Birthday import Birthday
from .Email import Email


class Record:
    def __init__(self):
        self.phones = []
        self.emails = []
        self.birthday = ''

        # Додаємо ім'я контакту
        while True:
            name_input = input("Please type contact's name: ")
            try:
                self.name = Name(name_input)
                break
            except ValueError as e:
                print(e)

        # Додаємо номер телефону
        while True:
            phone_input = input("Please type contact's phone: ")
            try:
                self.phones.append(Phone(phone_input))
                break
            except ValueError as e:
                print(e)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_email(self, email):
        self.emails.append(Email(email))

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def get_phone_numbers(self):
        return [(index + 1, phone.value) for index, phone in enumerate(self.phones)]

    def get_emails(self):
        return [(index + 1, email.value) for index, email in enumerate(self.emails)]

    def delete_phone(self, index):
        return self.phones.pop(index)

    def delete_email(self, index):
        return self.emails.pop(index)

    def __str__(self):
        birthday_str = str(self.birthday).split()[0] if self.birthday else ''
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {birthday_str}, emails: {'; '.join(e.value for e in self.emails)}"