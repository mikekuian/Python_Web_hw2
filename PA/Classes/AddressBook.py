from collections import UserDict
from .Name import Name
from .Birthday import Birthday
from datetime import date, datetime, timedelta


class AddressBook(UserDict):
    def __init__(self):
        self.contacts = {}

    def add_contact(self, record):
        record_exists = None
        for contact in self.contacts.values():
            if str(record.name) == str(contact.name):
                record_exists = True
                break
        if record_exists:
            print('Contact with this name already exists')
        else:
            self.contacts[record.name] = record
            print("New contact successfully added")

    def print_contacts(self):
        for contact in self.contacts.values():
            print(contact)

    def search_record_by_name(self, contact_name):
        record = None
        for contact in self.contacts.values():
            if contact_name == str(contact.name):
                record = contact
                break
        return record

    def search_records_by_name(self, search_query):
        records = []
        for contact in self.contacts.values():
            if str(contact.name).casefold().__contains__(search_query.casefold()):
                records.append(contact)
        return records

    def add_email(self):
        input_name = input("Enter the name of the contact: ")
        record = self.search_record_by_name(input_name)
        if record:
            while True:
                try:
                    email_input = input(f"Enter email for {record.name}: ")
                    record.add_email(email_input)
                    print(f"Email '{email_input}' added to the contact '{record.name}'")
                    break
                except ValueError as e:
                    print(e)
        else:
            print(f"Contact with name '{input_name}' not found")

    def add_birthday(self):
        input_name = input("Enter the name of the contact: ")
        record = self.search_record_by_name(input_name)
        if record:
            while True:
                try:
                    birthday_input = input(f"Enter birthday for {record.name}: ")
                    record.add_birthday(birthday_input)
                    print(f"Birthday '{birthday_input}' added to the contact '{record.name}'")
                    break
                except ValueError as e:
                    print(e)
        else:
            print(f"Contact with name '{input_name}' not found")

    def add_phone(self):
        input_name = input("Enter the name of the contact: ")
        record = self.search_record_by_name(input_name)
        if record:
            while True:
                try:
                    phone_input = input(f"Enter a new phone for the contact '{record.name}' to add: ")
                    record.add_phone(phone_input)
                    print(f"Phone '{phone_input}' was successfully added to the contact '{record.name}'")
                    break
                except ValueError as e:
                    print(e)
        else:
            print(f"Contact with name '{input_name}' not found")

    def delete_phone(self):
        input_name = input("Enter the name of the contact: ")
        record = self.search_record_by_name(input_name)
        if record:
            print(f"Here's a list of the phones for the contact '{input_name}':")
            phones_list = record.get_phone_numbers()
            for row in phones_list:
                print(f'{row[0]}: {row[1]}')
            while True:
                phone_index_input = int(input('Enter the index of the phone you want to delete: '))
                if phone_index_input < 1 or phone_index_input > len(phones_list):
                    print(f'Index is out of the range. You have to enter index in the range of [1 - {len(phones_list)}]')
                elif len(phones_list) == 1:
                    print("It has to be at least 1 phone number, you can't delete it")
                    break
                elif 1 <= phone_index_input <= len(phones_list):
                    deleted_phone = record.delete_phone(phone_index_input - 1)
                    print(f'Phone number {deleted_phone} was successfully deleted')
                    break
        else:
            print(f"Contact with name '{input_name}' not found")

    def delete_email(self):
        input_name = input("Enter the name of the contact: ")
        record = self.search_record_by_name(input_name)
        if record:
            print(f"Here's a list of the emails for the contact '{input_name}':")
            emails_list = record.get_emails()
            for row in emails_list:
                print(f'{row[0]}: {row[1]}')
            while True:
                email_index_input = int(input('Enter the index of the email you want to delete: '))
                if email_index_input < 1 or email_index_input > len(emails_list):
                    print(f'Index is out of the range. You have to enter index in the range of [1 - {len(emails_list)}]')
                elif 1 <= email_index_input <= len(emails_list):
                    deleted_email = record.delete_email(email_index_input - 1)
                    print(f'Email {deleted_email} was successfully deleted')
                    break
        else:
            print(f"Contact with name '{input_name}' not found")

    def delete_contact(self):
        input_name = input("Enter the name of the contact: ")
        record = self.search_record_by_name(input_name)
        if record:
            key_to_delete = None
            for key, value in self.contacts.items():
                if str(value.name) == input_name:
                    key_to_delete = key
                    break
            if key_to_delete:
                del self.contacts[key_to_delete]
                print(f"Contact '{input_name}' successfully deleted")
        else:
            print(f"Contact '{input_name}' not found in the address book")

    def search_contacts(self):
        query = input("Enter some text: ")
        records = self.search_records_by_name(query)
        if len(records) > 0:
            for record in records:
                print(record)
        else:
            print('Nothing found')

    def edit_name(self):
        input_name = input("Enter the name of the contact: ")
        record = self.search_record_by_name(input_name)
        if record:
            while True:
                try:
                    new_name = input(f"Enter a new name for the contact '{record.name}': ")
                    record.name = Name(new_name)
                    print('Name was successfully changed')
                    break
                except ValueError as e:
                    print(e)
        else:
            print(f"Contact '{input_name}' not found in the address book")

    def search_birthdays(self):
        while True:
            try:
                interval_days = int(input('Enter the period for which you need to know birthday people in days: '))
                break
            except ValueError:
                print("Value is not a number")
        records = []
        current_datetime = datetime.now().date()
        today_year = current_datetime.year
        interval = timedelta(days=interval_days)
        end_period_of_birthday = current_datetime + interval
        for birth in self.contacts.values():
            true_birthday = birth.birthday
            if true_birthday:
                birthday_datetime = datetime.strptime(str(true_birthday), '%Y-%m-%d %H:%M:%S')
                new_birthday_date = birthday_datetime.date().replace(year=today_year)
                new_new_birthday_date = birthday_datetime.date().replace(year=today_year + 1)
                if current_datetime <= new_birthday_date <= end_period_of_birthday or current_datetime <= new_new_birthday_date <= end_period_of_birthday:
                    records.append(birth)
        if len(records) > 0:
            for record in records:
                print(record)
        else:
            print(f"For {interval_days} days, you have no contacts with birthdays")
