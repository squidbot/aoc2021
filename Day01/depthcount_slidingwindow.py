with open('input.txt') as f:
    lines = f.readlines()
    count = 0
    prevSum = 0
    for i in range(len(lines)):
        if i + 3 > len(lines):
            break
        newSum = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
        if prevSum != 0:
            if newSum > prevSum:
                count += 1
        prevSum = newSum
    print(count)
