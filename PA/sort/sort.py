from pathlib import Path
import re
import shutil
import tarfile
import zipfile
import gzip
import os


class FileSorted:
    try:
        path_input = Path(input('Enter the path to the directory: '))
    except FileNotFoundError:
        print("Invalid path")
    # path_to_sort = Path('sort\\files_to_sort')
    # path_sorted = Path('sort\\files_to_sort\\')
    path_to_sort = path_input
    path_sorted = path_input
    UKRAINIAN_SYMBOLS = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "je", "zh", "z", "y", "i",
                   "ji", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                   "f", "h", "ts", "ch", "sh", "sch", "", "ju", "ja")

    TRANS = {}
    for key, value in zip(UKRAINIAN_SYMBOLS, TRANSLATION):
        TRANS[ord(key)] = value
        TRANS[ord(key.upper())] = value.upper()

    images = list()
    videos = list()
    documents = list()
    music = list()
    folders = list()
    archives = list()
    others = list()
    unknown = set()
    extensions = set()

    registered_extensions = {
        'JPEG': images,
        'JPG': images,
        'PNG': images,
        'SVG': images,
        'AVI': videos,
        'MP4': videos,
        'MOV': videos,
        'MKV': videos,
        'DOC': documents,
        'DOCX': documents,
        'TXT': documents,
        'PDF': documents,
        'XLSX': documents,
        'PPTX': documents,
        'MP3': music,
        'OGG': music,
        'WAV': music,
        'AMR': music,
        'ZIP': archives,
        'GZ': archives,
        'TAR': archives
    }

    for key, value in zip(UKRAINIAN_SYMBOLS, TRANSLATION):
        TRANS[ord(key)] = value
        TRANS[ord(key.upper())] = value.upper()

    # Метод перетворює українські символи в їхні латинські еквіваленти.
    def normalize(self, name):
        name, *extension = name.split('.')
        new_name = name.translate(self.TRANS)
        new_name = re.sub(r'\W', "_", new_name)
        return f"{new_name}.{'.'.join(extension)}"

    # Метод призначений для отримання розширення файлу
    def get_extensions(self, file_name):
        return Path(file_name).suffix[1:].upper()

    # Метод призначений для сканування та визначення типів файлів на основі їх розширень
    def scan(self, folder):
        for item in folder.iterdir():
            if item.is_dir():
                if item.name not in ('archives', 'music', 'documents', 'videos', 'images'):
                    self.folders.append(item)
                    self.scan(item)
                continue
            extension = self.get_extensions(file_name=item.name)
            new_name = folder/item.name
            if not extension:
                self.others.append(new_name)
            else:
                try:
                    container = self.registered_extensions[extension]
                    self.extensions.add(extension)
                    container.append(new_name)
                except KeyError:
                    self.unknown.add(extension)
                    self.others.append(new_name)

    #  Метод призначений для обробки знайдених файлів.
    def handle_file(self, path, dist):
        # target_folder = root_folder / dist
        target_folder = self.path_sorted / dist
        target_folder.mkdir(exist_ok=True)
        path.replace(target_folder/self.normalize(path.name))

    #  Метод призначений для обробки знайдених архівів.
    def handle_archive(self, path, dist):
        # target_folder = root_folder / dist
        target_folder = self.path_sorted / dist
        target_folder.mkdir(exist_ok=True)
        new_name = self.normalize(path.name.replace(
            ".zip", "").replace(".gz", "").replace(".tar", ""))
        archive_folder = target_folder / new_name
        archive_folder.mkdir(exist_ok=True)
        try:
            shutil.unpack_archive(str(path.resolve()),
                                  str(archive_folder.resolve()))
            os.remove(path)
        except (shutil.ReadError, FileNotFoundError, tarfile.ReadError, zipfile.BadZipFile, gzip.BadGzipFile):
            archive_folder.rmdir()
            return

    # Видалення порожніх папок
    def remove_empty_folders(self, path):
        for item in path.iterdir():
            if item.is_dir():
                self.remove_empty_folders(item)
                try:
                    item.rmdir()
                except OSError:
                    pass

    # Метод видаляє порожні папки всередині заданої папки.
    def get_folder_objects(self, root_path):
        for folder in root_path.iterdir():
            if folder.is_dir():
                self.remove_empty_folders(folder)
                try:
                    folder.rmdir()
                except OSError:
                    pass

    def clean_folder(self):
        folder_path = self.path_to_sort
        print(f"Start sorting files...")
        self.scan(folder_path)

        for file in self.images:
            self.handle_file(file, "images")

        for file in self.videos:
            self.handle_file(file, "videos")

        for file in self.documents:
            self.handle_file(file, "documents")

        for file in self.music:
            self.handle_file(file, "music")

        for file in self.others:
            self.handle_file(file, "others")

        for file in self.archives:
            self.handle_archive(file, "archives")

        self.get_folder_objects(folder_path)

        print('Sorting finished')

if __name__ == '__main__':
    sorter = FileSorted()
    sorter.clean_folder()
