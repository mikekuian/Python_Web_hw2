from abc import ABC, abstractmethod


class Note:
    def __init__(self, text, tags=None):
        self.text = text
        self.tags = tags

    def __str__(self):
        if self.tags == None:
            self.tags = ''
        return f"Text: {self.text}, tags: {self.tags}"


class AbstractPersonalNoteAssistant(ABC):

    @abstractmethod
    def execute(self, assistant):
        pass


class AddNoteCommand(AbstractPersonalNoteAssistant):

    def execute(self, assistant):
        text = input(f"Enter a new note text: ")
        wait_for_tags = input(f"Do you like to add some tags? (y/n)? ")
        while True:
            if wait_for_tags.casefold() == 'y':
                tags = input('Enter tags (comma separated): ')
                note = Note(text, tags)
                assistant.notes.append(note)
                break
            elif wait_for_tags.casefold() == 'n':
                note = Note(text)
                assistant.notes.append(note)
                break
            elif wait_for_tags.casefold() != 'y' or wait_for_tags.casefold() != 'n':
                wait_for_tags = input('Please type y or n: ')
        print("Note was successfully added")


class EditNoteCommand(AbstractPersonalNoteAssistant):
    def execute(self, assistant):
        print(f"Here's a list of your notes:")
        assistant.print_notes()
        while True:
            index = int(input('Enter the index of the note you want to edit: '))
            if index < 1 or index > len(assistant.notes):
                print(f'Index is out of the range. You have to enter index in the range of [1 - {len(assistant.notes)}]')
            elif 1 <= index <= len(assistant.notes):
                new_text = input('Enter the new text for the note: ')
                wait_for_tags = input(f"Do you like to modify the tags? (y/n)? ")
                if wait_for_tags.casefold() == 'y':
                    tags = input('Enter tags (comma separated): ')
                    new_note = Note(new_text, tags)
                    assistant.notes[index - 1] = new_note
                    print("Note was successfully modified")
                    break
                elif wait_for_tags.casefold() == 'n':
                    old_tags = assistant.notes[index - 1].tags
                    new_note = Note(new_text, old_tags)
                    assistant.notes[index - 1] = new_note
                    print("Note was successfully modified")
                    break
                elif wait_for_tags.casefold() != 'y' or wait_for_tags.casefold() != 'n':
                    wait_for_tags = input('Please type y or n: ')


class DeleteNoteCommand(AbstractPersonalNoteAssistant):
    def execute(self, assistant):
        print(f"Here's a list of your notes:")
        assistant.print_notes()
        while True:
            index = int(input('Enter the index of the note you want to delete: '))
            if index < 1 or index > len(assistant.notes):
                print(f'Index is out of the range. You have to enter index in the range of [1 - {len(assistant.notes)}]')
            elif 1 <= index <= len(assistant.notes):
                del assistant.notes[index - 1]
                print(f'Note was successfully deleted')
                break


class SearchNotesCommand(AbstractPersonalNoteAssistant):
    def execute(self, assistant):
        keyword = input('Enter some text: ')
        matching_notes = []
        for note in assistant.notes:
            if note.text.casefold().__contains__(keyword.casefold()):
                matching_notes.append(note)
        if len(matching_notes) == 0:
            print(f'No notes found with the keyword "{keyword}".')
        else:
            print(f'Search results for the keyword "{keyword}":')
            for note in matching_notes:
                print(note)


class SearchNotesByTagCommand(AbstractPersonalNoteAssistant):
    def execute(self, assistant):
        tag = input('Enter tag(s) (comma separated): ')
        tag_parts = [part.strip() for part in tag.split(',')]
        matching_notes = [note for note in assistant.notes if all(
            tag_part in note.tags for tag_part in tag_parts)]
        if len(matching_notes) == 0:
            print(f'No notes found with tag(s) "{tag}"')
        else:
            print(f'Searching results for tag(s) "{tag}":')
        for note in matching_notes:
            print(note)


class PrintNotesCommand(AbstractPersonalNoteAssistant):
    def execute(self, assistant):
        assistant.print_notes()


class PersonalNoteAssistant:

    def __init__(self):
        self.notes = []

    def execute_command(self, command):
        command.execute(self)

    def print_notes(self):
        for index, note in enumerate(self.notes):
            print(f'{index + 1}: {note}')
