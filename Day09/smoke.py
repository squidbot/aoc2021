def smoke1(heightmap):
    count = 0
    for y in range(1, len(heightmap) - 1):
        for x in range(1, len(heightmap[0]) - 1):
            if heightmap[y][x] < heightmap[y - 1][x] and\
                heightmap[y][x] < heightmap[y + 1][x] and\
                heightmap[y][x] < heightmap[y][x - 1] and\
                heightmap[y][x] < heightmap[y][x + 1]:
                    count += heightmap[y][x] + 1
    print("Count is", count)

def smoke2(heightmap):
    counts = []
    marked = [[0] * len(heightmap[0]) for _ in range(len(heightmap))]
    for y in range(1, len(heightmap) - 1):
        for x in range(1, len(heightmap[0]) - 1):
            if heightmap[y][x] < heightmap[y - 1][x] and\
                heightmap[y][x] < heightmap[y + 1][x] and\
                heightmap[y][x] < heightmap[y][x - 1] and\
                heightmap[y][x] < heightmap[y][x + 1]:
                    #start of basin is [y][x]
                    count = 1
                    queue = []
                    queue.append([y, x])
                    heightmap[y][x] = 9
                    while queue:
                        curDepth = queue.pop()
                        py = curDepth[0]
                        px = curDepth[1]
                        if heightmap[py - 1][px] != 9:
                            count += 1
                            heightmap[py - 1][px] = 9
                            queue.append([py - 1, px])
                        if heightmap[py + 1][px] != 9:
                            count += 1
                            heightmap[py + 1][px] = 9
                            queue.append([py + 1, px])
                        if heightmap[py][px - 1] != 9:
                            count += 1
                            heightmap[py][px - 1] = 9
                            queue.append([py, px - 1])
                        if heightmap[py][px + 1] != 9:
                            count += 1
                            heightmap[py][px + 1] = 9
                            queue.append([py, px + 1])
                    print("Count =", count)
                    counts.append(count)
    counts.sort()
    print(counts)
    print("Product =", counts[-1] * counts[-2] * counts[-3])

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()
        heightmap = []
        # frame the heightmp with 9's so we don't need to worry about checking edges
        heightmap.append([9] * (len(lines[0]) + 2))
        for line in lines:
            hmline = [int(i) for i in line]
            hmline.insert(0, 9)
            hmline.append(9)
            heightmap.append(hmline)
        heightmap.append([9] * (len(lines[0]) + 2))
        smoke1(heightmap)
        smoke2(heightmap)
