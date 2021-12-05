def ventIntersections2() -> None:
    with open('input.txt') as f:
        lines = f.read().splitlines()
        coordPairs = []
        for line in lines:
            coordStrs = line.split(' -> ')
            coordPair = (tuple(int(v) for v in coordStrs[0].split(',')), tuple(int(v) for v in coordStrs[1].split(',')))
            coordPairs.append(coordPair)

        # determine if line is horizontal or vertical or diagonal
        # determine all points along line and increment count in map on the tuple
        # count all entries > 1
        grid = {}
        for coordPair in coordPairs:
            pair1 = coordPair[0]
            pair2 = coordPair[1]
            if pair1[0] == pair2[0]:
                r = None
                if pair1[1] > pair2[1]:
                    r = range(pair2[1], pair1[1] + 1)
                else:
                    r = range(pair1[1], pair2[1] + 1)
                for i in r:
                    gridCoord = (pair1[0], i)
                    grid[gridCoord] = grid.get(gridCoord, 0) + 1

            elif pair1[1] == pair2[1]:
                #horizontal line
                r = None
                if pair1[0] > pair2[0]:
                    r = range(pair2[0], pair1[0] + 1)
                else:
                    r = range(pair1[0], pair2[0] + 1)
                for i in r:
                    gridCoord = (i, pair1[1])
                    grid[gridCoord] = grid.get(gridCoord, 0) + 1

            else:
                #diagonal line
                rx = None
                if pair1[0] > pair2[0]:
                    rx = range(pair1[0], pair2[0] - 1, -1)
                else:
                    rx = range(pair1[0], pair2[0] + 1)

                ry = None
                if pair1[1] > pair2[1]:
                    ry = range(pair1[1], pair2[1] - 1, -1)
                else:
                    ry = range(pair1[1], pair2[1] + 1)

                for x,y in zip(rx, ry):
                    gridCoord = (x, y)
                    grid[gridCoord] = grid.get(gridCoord, 0) + 1

        count = 0
        for value in grid.values():
            if value > 1:
                count += 1

        print(count)  
        
def ventIntersections() -> None:
    with open('input_test.txt') as f:
        lines = f.read().splitlines()
        coordPairs = []
        for line in lines:
            coordStrs = line.split(' -> ')
            coordPair = (tuple(int(v) for v in coordStrs[0].split(',')), tuple(int(v) for v in coordStrs[1].split(',')))
            coordPairs.append(coordPair)

        # determine if line is horizontal or vertical or diagonal
        # reject diagonals
        # determine all points along line and increment count in map on the tuple
        # count all entries > 1
        grid = {}
        for coordPair in coordPairs:
            pair1 = coordPair[0]
            pair2 = coordPair[1]
            if pair1[0] == pair2[0]:
                r = None
                if pair1[1] > pair2[1]:
                    r = range(pair2[1], pair1[1] + 1)
                else:
                    r = range(pair1[1], pair2[1] + 1)
                for i in r:
                    gridCoord = (pair1[0], i)
                    grid[gridCoord] = grid.get(gridCoord, 0) + 1

            elif pair1[1] == pair2[1]:
                #horizontal line
                r = None
                if pair1[0] > pair2[0]:
                    r = range(pair2[0], pair1[0] + 1)
                else:
                    r = range(pair1[0], pair2[0] + 1)
                for i in r:
                    gridCoord = (i, pair1[1])
                    grid[gridCoord] = grid.get(gridCoord, 0) + 1
        
        count = 0
        for value in grid.values():
            if value > 1:
                count += 1
        
        print(count)

              


if __name__ == '__main__':
    ventIntersections2()

"""         
            for y in range(10):
            for x in range(10):
                print(grid.get((x,y), '.'), end='')
            print()
 """
