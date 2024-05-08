import csv
import json
import pickle
import sys
import os

class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

class CSVHandler(FileHandler):
    def load_data(self):
        with open(self.file_path, "r") as csv_file:
            return list(csv.reader(csv_file))

    def save_data(self, data):
        with open(self.file_path, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(data)

class JSONHandler(FileHandler):
    def load_data(self):
        with open(self.file_path, "r") as json_file:
            return json.load(json_file)

    def save_data(self, data):
        with open(self.file_path, "w") as json_file:
            json.dump(data, json_file)

class PickleHandler(FileHandler):
    def load_data(self):
        with open(self.file_path, "rb") as pickle_file:
            return pickle.load(pickle_file)

    def save_data(self, data):
        with open(self.file_path, "wb") as pickle_file:
            pickle.dump(data, pickle_file)

def get_file_handler(file_path):
    _, extension = os.path.splitext(file_path)
    if extension == ".csv":
        return CSVHandler(file_path)
    elif extension == ".json":
        return JSONHandler(file_path)
    elif extension == ".pickle":
        return PickleHandler(file_path)
    else:
        print("Unsupported file type.")
        sys.exit()

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) < 4:
        print("Usage: Python prog2.py <src> <dst> <change1> <change2> ...")
        sys.exit()

    old_file = sys.argv[1]
    new_file = sys.argv[2]
    changes = sys.argv[3:]

    file_handler = get_file_handler(old_file)
    old_data = file_handler.load_data()

    # Now apply changes to the old_data based on the provided arguments
    for change in changes:
        x, y, value = change.split(",")
        old_data[int(y)][int(x)] = value

    # Save the modified data to the new file
    file_handler = get_file_handler(new_file)
    file_handler.save_data(old_data)


