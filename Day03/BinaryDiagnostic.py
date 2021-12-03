def diagnostic1() -> None:
    with open('input.txt') as f:
        lines = f.read().splitlines()
        lenLine = len(lines[0]) #all lines have equal count (12) but why not use good practices!
        print("Line length is", lenLine)
        onesCount = [0] * lenLine # array to hold count of 1's in each position
        for line in lines:
            for pos in range(lenLine):
                if line[pos] == '1':
                    onesCount[pos] += 1
        numLines = len(lines)
        print("Number of lines", numLines)
        gammaStr = ""
        for pos in range(lenLine):
            print("Count of ones for position", pos, "is", onesCount[pos])
            if numLines - onesCount[pos] < onesCount[pos]:
                gammaStr += "1"
            else:
                gammaStr += "0"
        print("Gamma string is ", gammaStr)
        gamma = int(gammaStr, 2)
        epsilonStr = ""
        for pos in range(lenLine):
            if gammaStr[pos] == "0":
                epsilonStr += "1"
            else:
                epsilonStr += "0"
        epsilon = int(epsilonStr, 2)
        print("Epsilon string is", epsilonStr)
        print("Gamma is", gamma, "Epsilon is", epsilon)
        print("Power consumption is", gamma * epsilon)

def findRating(lines, predicate, lenLine, testBitPos) -> int:
    zeroList = []
    oneList = []
    useList = None
    #first find most common bit in current position
    #also, store the lists of 0 and 1 bit so we don't need to pass through twice
    #just recurse with the needed list and discard the other
    onesCount = 0
    for line in lines:
        if line[testBitPos] == "1":
            onesCount += 1
            oneList.append(line)
        else:
            zeroList.append(line)
    if predicate(len(lines), onesCount):
        useList = oneList
    else:
        useList = zeroList
    if len(useList) == 1:
        return int(useList[0], 2)
    else:
        return findRating(useList, predicate, lenLine, testBitPos + 1)

def diagnostic2() -> None:
    with open('input.txt') as f:
        lines = f.read().splitlines()
        lenLine = len(lines[0]) #all lines have equal count (12) but why not use good practices!
        print("Line length is", lenLine)
        oxygenRating = findRating(lines, lambda a,b: a-b <= b ,lenLine, 0)
        print("Oxygen rating is", oxygenRating)
        c02Rating = findRating(lines, lambda a,b: a-b > b, lenLine, 0)
        print("C02 rating is", c02Rating)
        print("Life support rating is", oxygenRating * c02Rating)

if __name__ == '__main__':
    print("Diagnostic 1")
    print("------------")
    diagnostic1()
    print("\nDiagnostic 2")
    print("------------")
    diagnostic2()
