def parse_lines(lines):
    reading_dots = True
    dots = set()
    folds = []
    for line in lines:
        if not line:
            reading_dots = False
        else:
            if reading_dots:
                str_dot = line.split(',')
                dots.add((int(str_dot[0]), int(str_dot[1])))
            else:
                str_line = line[11:].split('=')
                folds.append([str_line[0], int(str_line[1])])
    return dots, folds

def origami1(dots, folds):
    fold_axes = {'x':0, 'y':1}
    fold = folds[0]

    folded_dots = set()
    removed_dots = set()
    for dot in dots:
        axis = fold_axes[fold[0]]
        if dot[axis] > int(fold[1]):
            removed_dots.add(dot)
            new_dot = None
            if axis == 0:
                new_dot = ((2*fold[1]) - dot[axis], dot[1])
            else:
                new_dot = (dot[0], (2*fold[1]) - dot[axis])
            folded_dots.add(new_dot)
    dots -= removed_dots
    dots |= folded_dots
    print("Num dots after fold =", len(dots))
        
def origami2(dots, folds):
    fold_axes = {'x':0, 'y':1}

    for fold in folds:
        folded_dots = set()
        removed_dots = set()
        for dot in dots:
            axis = fold_axes[fold[0]]
            if dot[axis] > int(fold[1]):
                removed_dots.add(dot)
                new_dot = None
                if axis == 0:
                    new_dot = ((2*fold[1]) - dot[axis], dot[1])
                else:
                    new_dot = (dot[0], (2*fold[1]) - dot[axis])
                folded_dots.add(new_dot)
        dots -= removed_dots
        dots |= folded_dots
    
    max_x = 0
    max_y = 0
    for dot in dots:
        max_x = max(dot[0], max_x)
        max_y = max(dot[1], max_y)
    grid = sorted(dots, key=lambda k:[k[0],k[1]])
    print("Bounds =", max_x, max_y)
    #print(grid)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x,y) in dots:
                print("O", end='')
            else:
                print(".", end='')
        print("")


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()
        dots, folds = parse_lines(lines)
#        origami1(dots, folds)
        origami2(dots, folds)
