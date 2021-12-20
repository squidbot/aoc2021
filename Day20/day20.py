def convert_to_number(algo):
    binstr = ''.join(['0' if char == '.' else '1' for char in algo])
    return int(binstr, 2)

def enhance1(iha, input_image, empty):
    num_rows = len(input_image) + 4
    num_cols = len(input_image[0]) + 4
    image = []
    for row in input_image:
        image.append([empty, empty] + list(row) + [empty, empty])
    image.insert(0, [empty for i in range(num_cols)])
    image.insert(0, [empty for i in range(num_cols)])
    image.append([empty for i in range(num_cols)])
    image.append([empty for i in range(num_cols)])

    output = []
    for row in range(1, num_rows - 1):
        out_row = []
        for col in range(1, num_cols - 1):
            lookup_raw = image[row - 1][col - 1] + \
                         image[row - 1][col] + \
                         image[row - 1][col + 1] + \
                         image[row][col - 1] + \
                         image[row][col] + \
                         image[row][col + 1] + \
                         image[row + 1][col - 1] + \
                         image[row + 1][col] + \
                         image[row + 1][col + 1]
            out_row.append(iha[convert_to_number(lookup_raw)])
        output.append(out_row)
    return output
            

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()

        iha = lines[0]
        out = enhance1(iha, lines[2:], '.')
        zit = '#'
        for i in range(49):
            out = enhance1(iha, out, zit)
            if zit == '#':
                zit = '.'
            else:
                zit = '#'

        count = 0
        for line in out:        
            for char in line:
                if char == '#':
                    count += 1
        
        print(count)

