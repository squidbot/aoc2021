import math
from os import set_inheritable

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

ex7 = [
    '[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]',
    '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]'
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
    #print("reducing", convert_to_string(num))
    pos = 0
    left_brace_count = 0
    for pos in range(len(num)):
        if num[pos] == '[':
            left_brace_count += 1
            if left_brace_count == 5:
                #print("Explode at position", pos + 1)
                num = explode(num, pos + 1)
                num = reduce(num)
                break
        elif num[pos] == ']':
            left_brace_count -= 1
    for pos in range(len(num)):
        if isinstance(num[pos], int) and num[pos] > 9:
            #print("Split at position", pos)
            num = split(num, pos)
            num = reduce(num)
            break

    return num

def add(num1, num2):
    return ['['] + num1 + num2 + [']']

def magnitude(num):
    stack = []
    mag = 0
    for entry in num:
        if entry == ']':
            r = stack.pop()
            l = stack.pop()
            mag = 3 * l + 2 * r
            stack.append(mag)
        elif entry == '[':
            pass
        else:
            stack.append(entry)
    return mag

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

def snailfish1(nums):
    sum = nums[0]
    for num in nums[1:]:
        print("summing", convert_to_string(sum), "and", convert_to_string(num))
        sum = add(sum, num)
        print("sum=", convert_to_string(sum))
        sum = reduce(sum)
        print("reduced=", convert_to_string(sum))
    
    print("Magnitude=", magnitude(sum))

def snailfish2(nums):
    mag = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                sum = add(nums[i], nums[j])
                sum = reduce(sum)
                m = magnitude(sum)
                if m > mag:
                    mag = m
    print(mag)


if __name__ == '__main__':
    with open('input.txt') as f:
        final_input = [convert_from_string(x) for x in f.read().splitlines()]
        #snailfish1(final_input)
        snailfish2(final_input)

        


