import random

def maze_game():
    print("🏰 Welcome to the Maze Escape Game!")
    print("You are trapped in a maze. Find the exit!")

  
    # Maze layout (E = exit, X = wall, . = path)
    maze = [
        [".", ".", ".", "X", "E"],
        ["X", "X", ".", "X", "X"],
        [".", ".", ".", ".", "."],
        ["X", ".", "X", "X", "."],
        [".", ".", ".", "X", "."]
    ]

    