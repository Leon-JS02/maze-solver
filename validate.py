"""Simple file validation functions."""

from os import path

DATA_DIR = "./data"


def validate_maze_text(file_name: str) -> bool:
    """Returns True if a valid maze text file exists within the 
    data directory of a given name."""
    valid_chars = list("SEW ")
    file_path = path.join(DATA_DIR, file_name)
    if not path.exists(file_path):
        return False

    with open(file_path, 'r', encoding='UTF-8') as f:
        maze_content = [line.strip() for line in f.readlines()]

    if not all([char in valid_chars for line in maze_content for char in line]):
        return False

    s_count = sum(line.count('S') for line in maze_content)
    e_count = sum(line.count('E') for line in maze_content)

    return s_count == 1 and e_count == 1


def validate_maze_image(file_name: str) -> bool:
    """Returns True if a valid maze png file exists within the data directory
    of a given name."""
    return path.exists(path.join(DATA_DIR, file_name))
