from collections import Counter, defaultdict

def parse(lines):
    template = lines[0]
    rules = {}
    for line in lines[2:]:
        rule = line.split(' -> ')
        rules[rule[0]] = rule[1]
    return template, rules

def insertion(template, rules):
    pair_counts = defaultdict(int)
    for index in range(len(template) - 1):
        pair_counts[template[index:index+2]] += 1
    for step in range(40):
        new_pair_counts = defaultdict(int)
        for pair, count in pair_counts.items():
            ins = rules[pair]
            new_pair_counts[pair[0] + ins] += count
            new_pair_counts[ins + pair[1]] += count
        pair_counts = new_pair_counts
    print(pair_counts)
    el_counts = defaultdict(int)
    for pair, count in pair_counts.items():
        el_counts[pair[0]] += count
    el_counts[template[-1]] += 1
    print(el_counts)
    print('Answer=', max(el_counts.values())- min(el_counts.values()))


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()
        template, rules = parse(lines)
        insertion(template, rules)