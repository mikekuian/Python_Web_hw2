Navigate to the project directory:
```cd Team-Project```

Install the package:
```pip install .```

Usage
To use the Personal Assistant, run the following command:

```PA```

This will start the digital assistant and you can interact with it to perform various tasks.
Here's a list of all the commands supported:

```
Contacts actions:
add_contact: Adds contact to the address book
edit_name: Edits the existing contact's name
add_phone: Adds new phone number to the existing contact
delete_phone: Delete phone number from the existing contact
add_birthday: Adds birthday to the existing contact
add_email: Adds email to the existing contact
delete_email: Deletes email from the existing contact
delete_contact: Deletes the existing contact
search_contacts: Searches contacts in the address book
search_birthdays: Search for contacts whose birthday will be in the coming days (the number of days is set)

Notes actions:
add_note: Adds note to the existing contact
edit_note: Edits the existing note
delete_note: Deletes the existing note
search_notes: Searches notes in the contacts

Tags actions:
search_tags: Searches notes by tags

Miscellaneous actions:
search_birthdays: Prints the list of contacts with birthdays in given amount of days
sort_files: Sort files in files directory
exit: Exit program
```

The logic is extremely simple - type any of the given commands above and follow further instructions.

License
This project is licensed under the MIT License - see the LICENSE file for details.
