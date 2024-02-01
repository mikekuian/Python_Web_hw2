class Note:
    def __init__(self, text, tags=None):
        self.text = text
        self.tags = tags

    def __str__(self):
        if self.tags == None:
            self.tags = ''
        return f"Text: {self.text}, tags: {self.tags}"


class PersonalNoteAssistant:
    def __init__(self):
        self.notes = []

    def add_note(self):
        text = input(f"Enter a new note text: ")
        wait_for_tags = input(f"Do you like to add some tags? (y/n)? ")
        while True:
            if wait_for_tags.casefold() == 'y':
                tags = input('Enter tags (comma separated): ')
                note = Note(text, tags)
                self.notes.append(note)
                break
            elif wait_for_tags.casefold() == 'n':
                note = Note(text)
                self.notes.append(note)
                break
            elif wait_for_tags.casefold() != 'y' or wait_for_tags.casefold() != 'n':
                wait_for_tags = input('Please type y or n: ')
        print("Note was successfully added")

    def edit_note(self):
        print(f"Here's a list of your notes:")
        self.print_notes()
        while True:
            index = int(input('Enter the index of the note you want to edit: '))
            if index < 1 or index > len(self.notes):
                print(f'Index is out of the range. You have to enter index in the range of [1 - {len(self.notes)}]')
            elif 1 <= index <= len(self.notes):
                new_text = input('Enter the new text for the note: ')
                wait_for_tags = input(f"Do you like to modify the tags? (y/n)? ")
                if wait_for_tags.casefold() == 'y':
                    tags = input('Enter tags (comma separated): ')
                    new_note = Note(new_text, tags)
                    self.notes[index - 1] = new_note
                    print("Note was successfully modified")
                    break
                elif wait_for_tags.casefold() == 'n':
                    old_tags = self.notes[index - 1].tags
                    new_note = Note(new_text, old_tags)
                    self.notes[index - 1] = new_note
                    print("Note was successfully modified")
                    break
                elif wait_for_tags.casefold() != 'y' or wait_for_tags.casefold() != 'n':
                    wait_for_tags = input('Please type y or n: ')

    def delete_note(self):
        print(f"Here's a list of your notes:")
        self.print_notes()
        while True:
            index = int(input('Enter the index of the note you want to delete: '))
            if index < 1 or index > len(self.notes):
                print(f'Index is out of the range. You have to enter index in the range of [1 - {len(self.notes)}]')
            elif 1 <= index <= len(self.notes):
                del self.notes[index - 1]
                print(f'Note was successfully deleted')
                break

    def search_notes(self):
        keyword = input('Enter some text: ')
        matching_notes = []
        for note in self.notes:
            if note.text.casefold().__contains__(keyword.casefold()):
                matching_notes.append(note)
        if len(matching_notes) == 0:
            print(f'No notes found with the keyword "{keyword}".')
        else:
            print(f'Search results for the keyword "{keyword}":')
            for note in matching_notes:
                print(note)

    def search_notes_by_tag(self):
        tag = input('Enter tag(s) (comma separated): ')
        tag_parts = [part.strip() for part in tag.split(',')]
        matching_notes = [note for note in self.notes if all(
            tag_part in note.tags for tag_part in tag_parts)]
        if len(matching_notes) == 0:
            print(f'No notes found with tag(s) "{tag}"')
        else:
            print(f'Searching results for tag(s) "{tag}":')
        for note in matching_notes:
            print(note)

    def print_notes(self):
        for index, note in enumerate(self.notes):
            print(f'{index + 1}: {note}')
