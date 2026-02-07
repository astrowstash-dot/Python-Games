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

# Player starting position
    player_pos = [0, 0]

    def print_maze():
        for i in range(len(maze)):
            row = ""
            for j in range(len(maze[i])):
                if [i, j] == player_pos:
                    row += "P "   # Player
                else:
                    row += maze[i][j] + " "
            print(row)
        print()
# Game loop
    while True:
        print_maze()
        move = input("Move (w=up, s=down, a=left, d=right): ").lower()

        new_pos = player_pos.copy()
            


    