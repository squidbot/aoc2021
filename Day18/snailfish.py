import math

ex1 = [
    '[[[[4,3],4],4],[7,[[8,4],9]]]',
    '[1,1]'
]

ex2 = [
    '[1,1]',
    '[2,2]',
    '[3,3]',
    '[4,4]'    
]

ex3 = [
    '[1,1]',
    '[2,2]',
    '[3,3]',
    '[4,4]',
    '[5,5]'    
]

ex4 = [
    '[1,1]',
    '[2,2]',
    '[3,3]',
    '[4,4]',
    '[5,5]',
    '[6,6]'    
]

ex5 = [
    '[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]',
    '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]',
    '[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]',
    '[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]',
    '[7,[5,[[3,8],[1,4]]]]',
    '[[2,[2,2]],[8,[8,1]]]',
    '[2,9]',
    '[1,[[[9,3],9],[[9,0],[0,7]]]]',
    '[[[5,[7,4]],7],1]',
    '[[[[4,2],2],6],[8,7]]'
]

ex6 = [
    '[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]',
    '[[[5,[2,8]],4],[5,[[9,9],0]]]',
    '[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]',
    '[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]',
    '[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]',
    '[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]',
    '[[[[5,4],[7,7]],8],[[8,3],8]]',
    '[[9,3],[[9,9],[6,[4,9]]]]',
    '[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]',
    '[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]'
]

def explode(num, pos):
    lnum = num[pos]
    rnum = num[pos + 1]
    
    for i in range(pos - 1, -1, -1):
        if isinstance(num[i], int):
            num[i] = num[i] + lnum
            break
    
    for i in range(pos+2, len(num)):
        if isinstance(num[i], int):
            num[i] = num[i] + rnum
            break
    
    return num[:pos-1] + [0] + num[pos+3:]
                
def split(num, pos):
    lnum = num[pos] // 2
    rnum = math.ceil(num[pos] / 2)
    return num[:pos] + ['[', lnum, rnum, ']'] + num[pos+1:]

def reduce(num):
    pos = 0
    left_brace_count = 0
    while pos < len(num):
        if num[pos] == '[':
            left_brace_count += 1
            if left_brace_count == 5:
                num = explode(num, pos + 1)
                num = reduce(num)
                break
        elif num[pos] == ']':
            left_brace_count -= 1
        else:
            if num[pos] > 9:
                num = split(num, pos)
                num = reduce(num)
                break
        pos += 1
    return num

def add(num1, num2):
    return ['['] + num1 + num2 + [']']

def magnitude(line):
    return 0

# it will be much easier to deal with a list of numbers and braces
def convert_from_string(line):
    number = []
    for char in line:
        if char.isdigit():
            number.append(int(char))
        elif char == '[' or char == ']':
            number.append(char)
        # safe to ignore commas as all input has single digits
    return number

def convert_to_string(num):
    line = ''
    for i, char in enumerate(num):
        if isinstance(char, int):
            line += str(char)
            if i < len(num) - 1 and num[i + 1] != ']':
                line += ','
        elif char == ']':
            line += ']'
            if i < len(num) - 1 and num[i + 1] != ']':
                line += ','
        else:
            line += '['
    return line

def snaifish1(nums):
    sum = nums[0]
    for num in nums[1:]:
        sum = add(sum, num)
        sum = reduce(sum)

    print(convert_to_string(sum))
    
    print("Magnitude=", magnitude(sum))

if __name__ == '__main__':
    with open('input.txt') as f:
        final_input = [convert_from_string(x) for x in f.read().splitlines()]
        
        snaifish1([convert_from_string(x) for x in ex3])
        #print(convert_to_string(explode(convert_from_string("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"), 18)))
        #print(convert_to_string(split(['[', '[', '[', '[',0,7, ']',4, ']','[', 15, '[', 0,13, ']', ']', ']','[', 1,1, ']',']'], 10)))

