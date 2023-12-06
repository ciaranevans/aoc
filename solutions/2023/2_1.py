import re

max_vals = {
    "blue": 14,
    "red": 12,
    "green": 13
}

if __name__ == '__main__':
    total = 0
    with open("../../data/2023/2_1.txt") as f:
        for line in f:
            possible = True
            game_and_choices = line.split(":")
            game_id = int(game_and_choices[0].replace("Game ", ""))
            choices = game_and_choices[1].split(";")
            for go in choices:
                match_red = re.search("(([0-9]+) red)", go)
                num_red = int(match_red.group(2)) if match_red else 0
                match_blue = re.search("(([0-9]+) blue)", go)
                num_blue = int(match_blue.group(2)) if match_blue else 0
                match_green = re.search("(([0-9]+) green)", go)
                num_green = int(match_green.group(2)) if match_green else 0
                if any([
                    max_vals.get("blue") < num_blue,
                    max_vals.get("red") < num_red,
                    max_vals.get("green") < num_green
                ]):
                    possible = False
            if possible:
                total += game_id
    print(total)