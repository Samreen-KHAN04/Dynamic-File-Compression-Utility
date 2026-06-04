import os


def read_text_file(filepath):

    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def write_text_file(filepath, data):

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(data)


def get_file_size(filepath):

    return os.path.getsize(filepath)