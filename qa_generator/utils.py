import os

def count_char(str, char):
    return sum(1 for c in str if c == char)


def get_all_file_paths(directory):
    file_paths = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            file_paths.append(full_path)
    return file_paths