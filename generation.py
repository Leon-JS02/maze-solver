"""File with functions to generate and read maze PNG images."""

from os import path

from PIL import Image

DATA_DIR = "./data"


def generate_maze_from_txt(file_path: str):
    """Generates a maze .png image from a .txt file."""
    pixel_map = {
        'S': (255, 0, 0),
        'E': (0, 255, 0),
        'W': (0, 0, 0),
        ' ': (255, 255, 255)
    }

    with open(path.join(DATA_DIR, file_path), 'r', encoding='UTF-8') as f:
        maze_chars = f.readlines()

    width = len(maze_chars[0]) - 1
    height = len(maze_chars)

    maze = Image.new("RGB", (width, height))
    pixels = maze.load()
    for y, line in enumerate(maze_chars):
        line = line.strip()
        for x, char in enumerate(line):
            pixels[x, y] = pixel_map[char]

    maze.save('data/maze.png')


def read_maze_from_png(file_path: str) -> str:
    """Returns a maze's content as a string from a PNG image."""
    character_map = {
        (255, 0, 0): 'S',
        (0, 255, 0): 'E',
        (0, 0, 0): 'W',
        (255, 255, 255): ' '
    }

    maze_image = Image.open(path.join(DATA_DIR, file_path))
    width, height = maze_image.size
    maze_text = ""

    for y in range(height):
        row = ""
        for x in range(width):
            pixel = maze_image.getpixel((x, y))
            row += character_map.get(pixel, '?')
        maze_text += row + "\n"

    return maze_text
