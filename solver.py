"""File for maze-solving logic."""
from os import path
from PIL import Image

DATA_DIR = "./data"


def get_source_and_destination(maze_rows: list[str]) -> list[tuple[int, int]]:
    """Returns the source and destination of the maze rows
    as a list of coordinate tuples."""
    source = dest = None
    for y in range(len(maze_rows)):
        for x in range(len(maze_rows[y])):
            if maze_rows[y][x] == 'S':
                source = (x, y)
            if maze_rows[y][x] == 'E':
                dest = (x, y)

    return [source, dest]


def get_valid_moves(current: tuple, maze: list, visited: set) -> list[tuple]:
    """Returns a list of valid positions reachable from the current location."""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = current
    valid_positions = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(maze) and 0 <= nx < len(maze[ny]):
            if maze[ny][nx] != 'W' and (nx, ny) not in visited:
                valid_positions.append((nx, ny))

    return valid_positions


def solve_maze(maze_text: str) -> list[tuple[int, int]]:
    """Uses DFS to solve the maze and returns a list representing the path for its solution."""
    maze_rows = maze_text.split("\n")
    start, end = get_source_and_destination(maze_rows)
    queue = [start]
    visited = set([start])
    parent = {}

    while queue:
        current = queue.pop()
        if current == end:
            return reconstruct_solution(parent, start, end)

        for move in get_valid_moves(current, maze_rows, visited):
            if move not in visited:
                visited.add(move)
                queue.append(move)
                parent[move] = current

    return None


def reconstruct_solution(parent: dict, start: tuple[int, int],
                         end: tuple[int, int]) -> list[tuple[int, int]]:
    """Reconstructs the maze solution from start to end using the parent dictionary."""
    solution = []
    current = end
    while current != start:
        solution.append(current)
        current = parent[current]
    solution.append(start)
    return solution


def overlay_solution(solution: list[tuple[int, int]], file_name: str):
    """Overlays the solution path on the maze image."""
    path_colour = (255, 127, 0)

    maze_img = Image.open(path.join(DATA_DIR, file_name))
    maze_pixels = maze_img.load()

    for x, y in solution:
        maze_pixels[x, y] = path_colour

    maze_img.save(path.join(DATA_DIR, f"solved_{file_name}"))
    print(f"Solution saved to {DATA_DIR}")
