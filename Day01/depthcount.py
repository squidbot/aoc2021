with open('input.txt') as f:
    lines = f.readlines()
    count = 0
    curDepth = 0
    for line in lines:
        newDepth = int(line)
        if curDepth != 0:
            if newDepth > curDepth:
                count += 1
        curDepth = newDepth
    print(count)
