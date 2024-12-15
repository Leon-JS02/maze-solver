"""The main command line script for the maze solver program."""

from argparse import ArgumentParser

from validate import validate_maze_text, validate_maze_image
from generation import generate_maze_from_txt, read_maze_from_png
from solver import solve_maze, overlay_solution


if __name__ == "__main__":
    parser = ArgumentParser(
        "Maze Solver", description="A CLI tool for generating and solving mazes.")
    parser.add_argument("-g", "--generate",
                        type=str, help="Generates a maze image from maze text.")
    parser.add_argument("-s", "--solve", type=str,
                        help="Solves a maze from its image representation.")
    args = parser.parse_args()

    if args.generate:
        if not validate_maze_text(args.generate):
            raise ValueError("Invalid maze file provided.")
        generate_maze_from_txt(args.generate)

    if args.solve:
        if not validate_maze_image(args.solve):
            raise ValueError("Invalid maze file provided.")
        maze_text = read_maze_from_png(args.solve)
        solution = solve_maze(maze_text)
        if not solution:
            raise ValueError("Maze is unsolvable!")
        overlay_solution(solution, args.solve)
