test_1 = [
"inp x",
"mul x -1"
]

test_2 = [
    "inp z",
    "inp x",
    "mul z 3",
    "eql z x"
]

test_3 = [
    "inp w",
    "add z w",
    "mod z 2",
    "div w 2",
    "add y w",
    "mod y 2",
    "div w 2",
    "add x w",
    "mod x 2",
    "div w 2",
    "mod w 2"
]

reg = {
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0
}

iptr = 0
data = None

def inp(a):
    global iptr
    reg[a] = int(data[iptr])
    iptr += 1

def add(a, b):
    reg[a] += b

def mul(a, b):
    reg[a] *= b

def div(a, b):
    reg[a] //= b

def mod(a, b):
    reg[a] %= b

def eql(a, b):
    reg[a] = 1 if reg[a] == b else 0    

inst_map = {
    'inp': inp,
    'add': add,
    'mul': mul,
    'div': div,
    'mod': mod,
    'eql': eql
}

def reset():
    global iptr
    iptr = 0
    for key in reg:
        reg[key] = 0
    global data
    data = ''

def print_reg():
    print("w", reg['w'], "x", reg['x'], "y", reg['y'], "z", reg['z'])

def run(_data, _code):
    reset()
    global data
    data = _data
    for line in _code:
        code = line.split()
        inst = code[0]
        a = code[1]
        if len(code) == 3:
            b = None
            try:
                b = int(code[2])
            except:
                b = reg[code[2]]            
            inst_map[inst](a, b)
        else:
            inst_map[inst](a)
        print(code, end='')
        print_reg()


if __name__ == '__main__':
    with open('input.txt') as f:
        puzzle_input = f.read().splitlines()
        
#        serial_number = str('39999698799429')
        serial_number = str('18116121134117')

        if not '0' in serial_number:
            run(serial_number, puzzle_input)
            print("s#", serial_number)
            print_reg()
            if reg['z'] == 0:
                print_reg()
                print("valid serial number =", serial_number)
