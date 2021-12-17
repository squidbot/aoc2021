def hex_to_binary(input):
    lut = { "0":"0000",
            "1":"0001",
            "2":"0010",
            "3":"0011",
            "4":"0100",
            "5":"0101",
            "6":"0110",
            "7":"0111",
            "8":"1000",
            "9":"1001",
            "A":"1010",
            "B":"1011",
            "C":"1100",
            "D":"1101",
            "E":"1110",
            "F":"1111"}
    output = []
    for hexdigit in input:
        output.append(lut[hexdigit])
    return ''.join(output)

def parse_version_count(input):
    print(input)
    version = int(input[:3], 2)
    id = int(input[3:6], 2)
    print("version", version, "id", id)
    if id == 4:
        size = 0
        for index in range(6, len(input), 5):
            size += 5
            if input[index] == 0:
                break 
        return version, size
    else:
        if input[6] == '0':
            pass
        else:
            pass


def decode1(line):
    full_message = hex_to_binary(line)
    print("Version sum is", parse_version_count(full_message))

    return
 
if __name__ == '__main__':
    with open('input_test.txt') as f:
        lines = f.read().splitlines()
        for line in lines:
            print(line)
            decode1(line)
