from Classes.Record import Record
from Classes.AddressBook import AddressBook
from Classes.Note import PersonalNoteAssistant, AddNoteCommand, EditNoteCommand, DeleteNoteCommand, SearchNotesCommand, SearchNotesByTagCommand
import pickle
import os


def handler():
    wait = True
    print('Type ? for help')
    while wait:
        inquire = input('>')
        parser(inquire)
        if inquire == '?':
            print(man)
        elif inquire == 'exit':
            wait = False


def parser(inquire):
    if inquire == 'add_contact':
        record = Record()
        address_book.add_contact(record)
        make_dump(book_name, address_book)
    elif inquire == 'print_contacts':
        address_book.print_contacts()
    elif inquire == 'add_email':
        address_book.add_email()
        make_dump(book_name, address_book)
    elif inquire == 'add_birthday':
        address_book.add_birthday()
        make_dump(book_name, address_book)
    elif inquire == 'add_phone':
        address_book.add_phone()
        make_dump(book_name, address_book)
    elif inquire == 'delete_phone':
        address_book.delete_phone()
        make_dump(book_name, address_book)
    elif inquire == 'delete_contact':
        address_book.delete_contact()
        make_dump(book_name, address_book)
    elif inquire == 'search_contacts':
        address_book.search_contacts()
    elif inquire == 'delete_email':
        address_book.delete_email()
        make_dump(book_name, address_book)
    elif inquire == 'edit_name':
        address_book.edit_name()
        make_dump(book_name, address_book)
    elif inquire == 'search_birthdays':
        address_book.search_birthdays()
    elif inquire == 'add_note':
        notes.execute_command(AddNoteCommand())
        make_dump(notes_name, notes)
    elif inquire == 'print_notes':
        notes.print_notes()
    elif inquire == 'delete_note':
        notes.execute_command(DeleteNoteCommand())
        make_dump(notes_name, notes)
    elif inquire == 'edit_note':
        notes.execute_command(EditNoteCommand())
        make_dump(notes_name, notes)
    elif inquire == 'search_notes':
        notes.execute_command(SearchNotesCommand())
    elif inquire == 'search_notes_by_tag':
        notes.execute_command(SearchNotesByTagCommand())
    elif inquire == 'sort_files':
        from ..sort.sort import FileSorted
        sorter = FileSorted()
        sorter.clean_folder()
    elif inquire == 'exit':
        pass
    elif inquire == '?':
        pass
    else:
        print('Something went wrong. Please try again')


def make_dump(name, object):
    with open(name, "wb") as f:
        pickle.dump(object, f)


project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

book_name = os.path.join(project_dir, "data", "book.bin")
book_size = os.path.getsize(book_name)

if book_size == 0:
    address_book = AddressBook()
else:
    with open(book_name, "rb") as book_file:
        address_book = pickle.load(book_file)


notes_name = os.path.join(project_dir, "data", "notes.bin")
notes_size = os.path.getsize(notes_name)

if notes_size == 0:
    notes = PersonalNoteAssistant()
else:
    with open(notes_name, "rb") as notes_file:
        notes = pickle.load(notes_file)

man_file = os.path.join(project_dir, "man.txt")

with open(man_file, 'r') as fh:
    man = fh.read()