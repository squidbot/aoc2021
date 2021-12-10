opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']
syntax_score = [3, 57, 1197, 25137]
complete_score = [1, 2, 3, 4]

def syntax1(lines):
    total_score = 0
    for line in lines:
        stack = []
        for i,v in enumerate(line):
            try:
                ind = opening.index(v)
                stack.append(ind)
            except ValueError:
                ind = closing.index(v)
                test = stack.pop()
                if ind != test:
                    total_score += syntax_score[ind]
                    break
    print(total_score)
    
def syntax2(lines):
    scores = []
    for line in lines:
        stack = []
        for i,v in enumerate(line):
            try:
                ind = opening.index(v)
                stack.append(ind)
            except ValueError:
                ind = closing.index(v)
                test = stack.pop()
                if ind != test:
                    stack.clear()
                    break   # ingore broken lines
        if len(stack) != 0:
            score = 0
            for v in reversed(stack):
                score = (score * 5) + complete_score[v]
            scores.append(score)
            print("Score for line = ", score)
    scores.sort()
    print(scores[int((len(scores)-1)/2)])    

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()

        #syntax1(lines)
        syntax2(lines)