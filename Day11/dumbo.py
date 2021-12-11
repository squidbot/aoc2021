SCAN_DIRECTIONS = [(-1,-1), (-1, 0), (-1, 1), (0, 1), (1,1), (1, 0), (1, -1), (0, -1)]

def dumbo1(playfield):
    flash_count = 0
    num_rows = len(playfield)
    num_cols = len(playfield[0])

    for step in range(100):
        # increase all by 1
        for row in range(num_rows):
            for col in range(num_cols):
                playfield[row][col] += 1

        flashed = set()
        while True:
            ten_count = 0 # we need to keep processing until there are no more 10+
            for row in range(num_rows):
                for col in range(num_cols):
                    if playfield[row][col] >= 10 and not (row, col) in flashed:
                        flashed.add((row, col))
                        flash_count += 1
                        playfield[row][col] += 1
                        for dir in SCAN_DIRECTIONS:
                            scan_row = row + dir[0]
                            scan_col = col + dir[1]
                            if scan_row >= 0 and scan_row < num_rows and scan_col >= 0 and scan_col < num_cols:
                                playfield[scan_row][scan_col] += 1
                                if playfield[scan_row][scan_col] == 10:
                                    ten_count += 1
            if ten_count == 0:
                break
        
        # clear all the >9 to 0
        print("Step ", step)
        for row in range(num_rows):
            for col in range(num_cols):
                if playfield[row][col] > 9:
                    playfield[row][col] = 0
                print(playfield[row][col], end='')
            print("")
        
    print("Number of flashes =", flash_count)

def dumbo2(playfield):
    flash_count = 0
    num_rows = len(playfield)
    num_cols = len(playfield[0])

    step = 0
    while True:
        # increase all by 1
        for row in range(num_rows):
            for col in range(num_cols):
                playfield[row][col] += 1

        flashed = set()
        while True:
            ten_count = 0 # we need to keep processing until there are no more 10+
            for row in range(num_rows):
                for col in range(num_cols):
                    if playfield[row][col] >= 10 and not (row, col) in flashed:
                        flashed.add((row, col))
                        flash_count += 1
                        playfield[row][col] += 1
                        for dir in SCAN_DIRECTIONS:
                            scan_row = row + dir[0]
                            scan_col = col + dir[1]
                            if scan_row >= 0 and scan_row < num_rows and scan_col >= 0 and scan_col < num_cols:
                                playfield[scan_row][scan_col] += 1
                                if playfield[scan_row][scan_col] == 10:
                                    ten_count += 1
            if ten_count == 0:
                break    

        # clear all the >9 to 0
        print("Step ", step)
        for row in range(num_rows):
            for col in range(num_cols):
                if playfield[row][col] > 9:
                    playfield[row][col] = 0
                print(playfield[row][col], end='')
            print("")

        zero_count = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if playfield[row][col] == 0:
                    zero_count += 1
        
        step += 1
        if zero_count == num_rows * num_cols:
            break

    print("Steps to simultaneous =", step)
    
if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()
        playfield = []
        for line in lines:
            playfield.append([int(i) for i in line])
        
        dumbo2(playfield)
 
'''
- First, the energy level of each octopus increases by 1.
- Then, any octopus with an energy level greater than 9 flashes.
    This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent.
    If this causes an octopus to have an energy level greater than 9, it also flashes. 
    This process continues as long as new octopuses keep having their energy level increased beyond 9. 
    (An octopus can only flash at most once per step.)
- Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.
'''
