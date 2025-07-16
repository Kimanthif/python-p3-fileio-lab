# lib/file_io.py

def write_file(file_name, file_content):
    full_name = file_name + ".txt"
    with open(full_name, "w") as file:
        file.write(file_content + "\n")


def append_file(file_name, append_content):
    full_name = file_name + ".txt"
    with open(full_name, "a") as file:
        file.write(append_content + "\n")


def read_file(file_name):
    full_name = file_name + ".txt"
    with open(full_name, "r") as file:
        return file.read().strip()  # remove any extra trailing newline
