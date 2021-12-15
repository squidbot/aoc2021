import time
import heapq

def g(a, b) -> float:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def neighbors(pos, max_row, max_col):
    n = []
    if pos[0] > 0:
        n.append((pos[0] - 1, pos[1]))
    if pos[0] < max_row:
        n.append((pos[0] + 1, pos[1]))
    if pos[1] > 0:
        n.append((pos[0], pos[1] - 1))
    if pos[1] < max_col:
        n.append((pos[0], pos[1] + 1))
    return n

def chiton1(map):
    goal = (len(map) - 1, len(map[0]) - 1)
    open = []
    heapq.heappush(open, ((0,0), 1))  #start at 0,0
    came_from = {(0,0):None}
    score = {(0,0):0}
    while open:
        current = heapq.heappop(open)[0]
        if current == goal:
            break
        for next in neighbors(current, goal[0], goal[1]):
            new_score = score[current] + map[current[0]][current[1]]
            if next not in score or new_score < score[next]:
                score[next] = new_score
                p = new_score + g(next, goal)
                heapq.heappush(open, (next, p))
                came_from[next] = current

    current = goal
    count = 0
    while current != (0,0):
        count += map[current[0]][current[1]]
        current = came_from[current]
    print(count)

def chiton2(map):
    new_map = []
    for r in range(5):
        for line in map:
            new_line = []
            for c in range(5):  
                for number in line:
                    new_number = number + c + r
                    if new_number > 9:
                        new_number = (new_number % 9) 
                    new_line.append(new_number)
            new_map.append(new_line)
    start = time.time()
    chiton1(new_map)   
    print(time.time() - start) 

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()
        map = []
        for line in lines:
            map.append([int(i) for i in line])
        #print("part one")
        #chiton1(map)

        print("part two")
        chiton2(map)



