def is_valid_move(maze, x, y):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0


def solve_maze(maze, start, end):
    def dfs(x, y):
        if (x, y) == end:
            return True

        if is_valid_move(maze, x, y):
            maze[x][y] = 2  # Mark the current cell as visited

            # Try moving in all possible directions
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if dfs(new_x, new_y):
                    return True

            # If no valid moves, backtrack
            maze[x][y] = 0  # Mark the current cell as unvisited
            return False

        return False

    start_x, start_y = start
    end_x, end_y = end

    if dfs(start_x, start_y):
        print("Maze solved!")
        for row in maze:
            print(row)
    else:
        print("No solution found.")


# Example maze (0 represents a valid path, 1 represents a wall)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start_point = (0, 0)
end_point = (4, 4)

solve_maze(maze, start_point, end_point)
