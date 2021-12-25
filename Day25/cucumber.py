test_1 = [
    "...>>>>>..."
]

test_2 = [
    "..........",
    ".>v....v..",
    ".......>..",
    ".........."
]

test_3 = [
    "...>...",
    ".......",
    "......>",
    "v.....>",
    "......>",
    ".......",
    "..vvv.."
]

test_4 = [
    "v...>>.vv>",
    ".vv>>.vv..",
    ">>.>v>...v",
    ">>v>>.>.v.",
    "v>v.vv.v..",
    ">.>>..v...",
    ".vv..>.>v.",
    "v.v..>>v.v",
    "....v..v.>"
]

def parse_lines(lines):
    grid = []
    for line in lines:
        grid.append(list(line))
    return grid

def print_grid(grid, iter):
    return
    print("Step", iter)
    for row in grid:
        print(''.join(row))
    print()
    
def cucumber1(grid):
    iter = 0
    print_grid(grid, iter)
    while True:
        iter += 1
        num_row = len(grid)
        num_col = len(grid[0])
        moved = False
        for row in range(num_row):
            unblocked = []
            for col in range(num_col):
                if grid[row][col] == '>':
                    check_col = col + 1 if col < num_col - 1 else 0
                    if grid[row][check_col] == '.':
                        unblocked.append(col)
            if unblocked:
                moved = True
                for ucol in unblocked:
                    check_col = ucol + 1 if ucol < num_col - 1 else 0
                    grid[row][ucol] = '.'
                    grid[row][check_col] = '>'

        for col in range(num_col):
            unblocked = []
            for row in range(num_row):
                if grid[row][col] == 'v':
                    check_row = row + 1 if row < num_row -1 else 0
                    if grid[check_row][col] == '.':
                        unblocked.append(row)
            if unblocked:
                moved = True
                for urow in unblocked:
                    check_row = urow + 1 if urow < num_row -1 else 0
                    grid[urow][col] = '.'
                    grid[check_row][col] = 'v'
        print_grid(grid, iter)
        #input()
        if not moved:
            print("No movement after", iter, "steps")
            break          

if __name__ == '__main__':
    with open('input.txt') as f:
        puzzle_lines = f.read().splitlines()
        
        #grid = parse_lines(test_1)
        #grid = parse_lines(test_2)
        #grid = parse_lines(test_3)
        #grid = parse_lines(test_4)
        grid = parse_lines(puzzle_lines)
        cucumber1(grid)
