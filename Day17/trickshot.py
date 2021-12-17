def simulate(xvel, yvel, xtmin, xtmax, ytmin, ytmax):
    if xvel == 0 and yvel == 0:
        return False, 0
    hit = False
    xpos = 0
    ypos = 0
    max_y = ytmin - 1
    while True:
        xpos += xvel
        ypos += yvel
        if ypos > max_y:
            max_y = ypos
        if xvel > 0:
            xvel -= 1
        elif xvel < 0:
            xvel += 1
        yvel -= 1
        if xpos >= xtmin and xpos <= xtmax and ypos >= ytmin and ypos <= ytmax:
            return True, max_y
        if xpos > xtmax or ypos < ytmin:
            return False, 0

    pass

def trickshot1(data):
    in_numbers = data[13:]
    in_coords = in_numbers.split(", ")
    in_xportion = in_coords[0][2:].split("..")
    xtmin, xtmax = int(in_xportion[0]), int(in_xportion[1])
    in_yportion = in_coords[1][2:].split("..")
    ytmin, ytmax = int(in_yportion[0]), int(in_yportion[1])

    max_y = ytmin - 1
    cur_max_x = 0
    cur_max_y = 0
    hit_count = 0
    for y in range(-xtmax, xtmax + 2):
        for x in range(xtmax + 2):
            hit, max = simulate(x, y, xtmin, xtmax, ytmin, ytmax)
            if hit:
                hit_count += 1
                if max > max_y:
                    max_y = max
                    cur_max_x = x
                    cur_max_y = y
    
    print("Max height is", max_y, "at x =", cur_max_x, "y =", cur_max_y)
    print("Hit count", hit_count)



if __name__ == '__main__':
    test_data = 'target area: x=20..30, y=-10..-5'
    real_data = 'target area: x=235..259, y=-118..-62'
    trickshot1(real_data)