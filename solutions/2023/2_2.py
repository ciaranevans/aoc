import re

max_vals = {
    "blue": 14,
    "red": 12,
    "green": 13
}

if __name__ == '__main__':
    total = 0
    with open("../../data/2023/2_1.txt") as f:
        power_sets = []
        for line in f:
            max_red = 0
            max_blue = 0
            max_green = 0
            game_and_choices = line.split(":")
            game_id = int(game_and_choices[0].replace("Game ", ""))
            choices = game_and_choices[1].split(";")
            for go in choices:
                match_red = re.search("(([0-9]+) red)", go)
                num_red = int(match_red.group(2)) if match_red else 0
                max_red = num_red if max_red < num_red else max_red
                match_blue = re.search("(([0-9]+) blue)", go)
                num_blue = int(match_blue.group(2)) if match_blue else 0
                max_blue = num_blue if max_blue < num_blue else max_blue
                match_green = re.search("(([0-9]+) green)", go)
                num_green = int(match_green.group(2)) if match_green else 0
                max_green = num_green if max_green < num_green else max_green
            power_sets.append(max_red*max_blue*max_green)
        total = sum(power_sets)
        print(total)