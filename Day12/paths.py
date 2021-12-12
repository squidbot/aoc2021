
def parse_lines(lines):
    nodes = {}
    for line in lines:
        input = line.split('-')
        if not input[0] in nodes.keys():
            nodes[input[0]] = [input[1]]
        else:
            nodes[input[0]].append(input[1])
        if not input[1] in nodes.keys():
            nodes[input[1]] = [input[0]]
        else:
            nodes[input[1]].append(input[0])
    return nodes

def follow_path1(nodes, current, visited, path, count):
    if current.islower():
        visited.add(current)
    path.append(current)
    
    if current == 'end':
        print(path)
        count += 1
    else:
        for edge in nodes[current]:
            if not edge in visited:
                count = follow_path1(nodes, edge, visited, path, count)
    path.pop()
    if current in visited:
        visited.remove(current)
    return count

def paths1(nodes):
    visited = set()
    path = []
    count = follow_path1(nodes, 'start', visited, path, 0)

    print("Path count =", count)
    return


def follow_path2(nodes, current, visited, path, count, test_cave, paths):
    if test_cave and current.islower():
        if current == test_cave:
            test_cave = None
        else:
            visited.add(current)
    elif current.islower():
        visited.add(current)
    path.append(current)
    
    if current == 'end':
        #print(path)
        paths.add("".join(path))
        count += 1
    else:
        for edge in nodes[current]:
            if not edge in visited:
                count = follow_path2(nodes, edge, visited, path, count, test_cave, paths)
    path.pop()
    if current in visited:
        visited.remove(current)
    return count

def paths2(nodes):
    visited = set()
    paths = set()
    path = []
    for key in nodes.keys():
        if key.islower() and key != 'start' and key != 'end':
            count = follow_path2(nodes, 'start', visited, path, 0, key, paths)
    print("Path count =", len(paths))
    return

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()
        nodes = parse_lines(lines)
#        paths1(nodes)
    paths2(nodes)
