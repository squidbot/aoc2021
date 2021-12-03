def drive() -> None:
    with open('input.txt') as f:
        lines = f.readlines()
        pos = 0
        depth = 0
        for line in lines:
            command, value = line.split(' ')
            value = int(value)
            match command[0]:
                case 'f':
                    pos += value
                case 'd':
                    depth += value
                case 'u':
                    depth -= value
        print("depth = ", depth, " pos = ", pos, " product = ", depth * pos)

def drive2() -> None:
    with open('input.txt') as f:
        lines = f.readlines()
        pos = 0
        aim = 0
        depth = 0
        for line in lines:
            command, value = line.split(' ')
            value = int(value)
            match command[0]:
                case 'f':
                    pos += value;
                    depth += value * aim;
                case 'd':
                    aim += value
                case 'u':
                    aim -= value
        
        print("depth = ", depth, " pos = ", pos, " product = ", depth * pos)


if __name__ == '__main__':
    drive2()
