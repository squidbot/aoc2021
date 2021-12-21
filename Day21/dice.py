test_input = [4, 8]
puzzle_input = [4, 9]

def part1():
    position = puzzle_input

    score = [0,0]
    die_roll = 0
    num_rolls = 0
    cur_player = 0

    while True:
        die_total = 0
        for _ in range(3):
            num_rolls += 1
            die_roll += 1
            if die_roll > 100:
                die_roll = 1
            die_total += die_roll
        for _ in range(die_total):
            position[cur_player] += 1
            if position[cur_player] > 10:
                position[cur_player] = 1
        score[cur_player] += position[cur_player]
        if score[cur_player] >= 1000:
            print("Game over, p1 score", score[0], "p2 score", score[1], "magic number", num_rolls * min(score[0],score[1]))
            break
        if cur_player == 0:
            cur_player = 1
        else:
            cur_player = 0

#part1()

import collections
def part2():
    position = puzzle_input
    roll_dist = collections.Counter(i + j + k for i in range(1,4) for j in range(1,4) for k in range(1,4))

    p1_wins = 0
    p2_wins = 0
    game_states = collections.defaultdict(int)
    game_states[(position[0], 0, position[1], 0)] = 1
    while game_states:
        updated_game_states = collections.defaultdict(int)
        for game_state in game_states:
            for roll in roll_dist:
                (pos1, score1, pos2, score2) = game_state
                pos1 = (pos1 + roll - 1) % 10 + 1
                score1 += pos1
                if score1 >= 21:
                    p1_wins += game_states[game_state] * roll_dist[roll]
                else:
                    updated_game_states[(pos1, score1, pos2, score2)] += game_states[game_state] * roll_dist[roll]
        game_states = updated_game_states

        updated_game_states = collections.defaultdict(int)
        for game_state in game_states:
            for roll in roll_dist:
                (pos1, score1, pos2, score2) = game_state
                pos2 = (pos2 + roll - 1) % 10 + 1
                score2 += pos2
                if score2 >= 21:
                    p2_wins += game_states[game_state] * roll_dist[roll]
                else:
                    updated_game_states[(pos1, score1, pos2, score2)] += game_states[game_state] * roll_dist[roll]
        game_states = updated_game_states
    
    print("p1 wins", p1_wins, "p2 wins", p2_wins)

part2()    

