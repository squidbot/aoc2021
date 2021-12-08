def segments1(output):
    digits = " ".join(output).split()
    count = 0
    # 1 = 2 segments
    # 4 = 4 segments
    # 7 = 3 segments
    # 8 = 7 segments
    countThese = [2,3,4,7]
    for digit in digits:
         if len(digit) in countThese:
             count += 1
    print("Simple digit count", count)

def segments2(patterns, output):
    """ 
    Digit   Num Segments    Segments
    0       6               a b c   e f g
    1       2                   c     f
    2       5               a   c d e   g
    3       5               a   c d   f g
    4       4                 b c d   f
    5       5               a b   d   f g
    6       6               a b   d e f g
    7       3               a   c     f
    8       7               a b c d e f g
    9       6               a b c d   f g

    1       2                   c     f
    4       4                 b c d   f
    7       3               a   c     f
    8       7               a b c d e f g

    2       5               a   c d e   g shares 2 with 7, 2 with 4, 1 with 1
    3       5               a   c d   f g shares 3 with 7, 3 with 4, 2 with 1
    5       5               a b   d   f g shares 2 with 7, 3 with 4, 1 with 1


    0       6               a b c   e f g shares 3 with 7, 3 with 4, 2 with 1
    6       6               a b   d e f g shares 2 with 7, 3 with 4, 1 with 1
    9       6               a b c d   f g shares 3 with 7, 4 with 4, 2 with 1

    """
    # determine which pattern each digit is 
        # determine the simples 1,4,7,8 first by number of segments
            # turn each in to frozenset
            # add frozenset, digit to dictionary
            # keep locals for 1 and 4 to use to compare rest of segments
        # look at 5 segments
            # if 2 segments match pattern 1, it's a 3
            # if 2 segments match pattern 4, it's a 2
            # if 3 segments match pattern 4, it's a 5 (no need to compare, this is final possibility)
            # turn each in to frozenset
        # look at 6 segments
            # if only 1 segments match pattern 1 it's a 6
            # if only 3 segments match pattern 4 it's a 0
            # if 4 segments match pattern 4 it's a 9 (n need to compare, this is final possiblity)
            # turn each in to frozenset
    # for list of outputs, turn in to a 4 digit number
        # in turn, mult by 1000, add to sum, nult by 100, etc
    # add each digit to a total count for answer
    totalCount = 0
    for i, pattern in enumerate(patterns):
        patternLookup = {}
        pattern1 = None
        pattern4 = None
        
        patternWords = pattern.split()
        patternWords.sort(key=len) # sort of hack but puts 2 and 4 in the list before 5 and 6
                            # so they have values when needed

        for word in patternWords:
            patternSet = frozenset(word)
            match len(word):
                case 2:
                    pattern1 = patternSet
                    patternLookup[pattern1] = 1
                case 4:
                    pattern4 = patternSet
                    patternLookup[pattern4] = 4
                case 3:
                    patternLookup[patternSet] = 7
                case 7:
                    patternLookup[patternSet] = 8
                case 5:
                    if len(patternSet & pattern1) == 2:
                        patternLookup[patternSet] = 3
                    elif len(patternSet & pattern4) == 2:
                        patternLookup[patternSet] = 2
                    else:
                        patternLookup[patternSet] = 5 
                case 6:
                    if len(patternSet & pattern1) == 1:
                        patternLookup[patternSet] = 6
                    elif len(patternSet & pattern4) == 3:
                        patternLookup[patternSet] = 0
                    else:
                        patternLookup[patternSet] = 9

        count = 0
        digit = 1000
        for word in output[i].split():
            count += patternLookup[frozenset(word)] * digit
            digit = int(digit / 10)
        totalCount += count
    print("Total count is", totalCount)    

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()
        patterns, output = map(list, zip(*[line.split(" | ") for line in lines]))

    segments1(output)
    segments2(patterns, output)
