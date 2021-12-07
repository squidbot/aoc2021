import sys
import statistics

def crabs():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        #load the called line and remove the line to make board parsing easier
        start_positions = [int(i) for i in lines[0].split(',')]
        max_start_pos = max(start_positions)
        min_start_pos = min(start_positions)
        print("Max start position =", max_start_pos, "Min start pos = ", min_start_pos)

        lowestCost = sys.maxsize
        lowestCostPosition = 0
        for potential_pos in range(min_start_pos, max_start_pos + 1):
            cost = 0
            for start_pos in start_positions:
                cost += abs(start_pos - potential_pos)
            print("Position =", potential_pos,"Cost =", cost)
            if cost < lowestCost:
                lowestCost = cost
                lowestCostPosition = potential_pos
        print("Lowest cost", lowestCost, "at position", lowestCostPosition)

def crabs2():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        #load the called line and remove the line to make board parsing easier
        start_positions = [int(i) for i in lines[0].split(',')]
        max_start_pos = max(start_positions)
        min_start_pos = min(start_positions)
        print("Max start position =", max_start_pos, "Min start pos = ", min_start_pos)

        lowestCost = sys.maxsize
        lowestCostPosition = 0
        for potential_pos in range(min_start_pos, max_start_pos + 1):
            cost = 0
            for start_pos in start_positions:
                distance = abs(start_pos - potential_pos)
                cost += int(distance * (distance + 1) / 2)
            print("Position =", potential_pos,"Cost =", cost)
            if cost < lowestCost:
                lowestCost = cost
                lowestCostPosition = potential_pos
        print("Lowest cost", lowestCost, "at position", lowestCostPosition)

def crabs3():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        #load the called line and remove the line to make board parsing easier
        start_positions = [int(i) for i in lines[0].split(',')]
        median = int(statistics.median(start_positions))
        print("Median =", median)
        cost = 0
        for pos in start_positions:
            cost += abs(pos - median)
        print("Cost = ", cost)


if __name__ == '__main__':
    crabs3()