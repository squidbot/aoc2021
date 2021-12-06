def lanternfish():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        fish_pop = [int(i) for i in lines[0].split(',')]

        for day in range(80):
            print("Simulating day", day, "population", len(fish_pop))
            fish_pop_new = fish_pop.copy()
            for i, fish in enumerate(fish_pop):
                if fish == 0:
                    fish_pop_new[i] = 6
                    fish_pop_new.append(8)
                else:
                    fish_pop_new[i] -= 1
            fish_pop = fish_pop_new
        print("Num Fish = ", len(fish_pop))

def lanternfish2():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        fish_pop_start = [int(i) for i in lines[0].split(',')]
        fish_pop = [0]*9
        for fish in fish_pop_start:
            fish_pop[fish] += 1
        
        for day in range(256):
            new_fish = fish_pop[0]
            for i in range(0, len(fish_pop)-1):
                fish_pop[i] = fish_pop[i+1]
            fish_pop[8] = new_fish
            fish_pop[6] += new_fish
        
        print("Num fish = ", sum(fish_pop))



if __name__ == '__main__':
    lanternfish2()