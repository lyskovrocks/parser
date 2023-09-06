import json
import os


class JsonDatabase:
    def __init__(self):
        self.file_path  = os.path.join(os.path.dirname(__file__), 'db.json')

        with open(self.file_path, 'r') as f:
            self.database = json.load(f)

    def save(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.database, f)

    def __save_back(self):
        with open(self.file_path + ".bak", 'w') as f:
            json.dump(self.database, f)

    def clear(self):
        self.database = {}

    def __del__(self):
    # Автосохранение при закрытии программы или уничтожении объекта
        self.__save_back()
