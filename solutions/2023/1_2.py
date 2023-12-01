import re

subs = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

if __name__ == "__main__":
    total = 0
    with open("../../data/2023/1_1.txt") as f:
        for line in f:
            digits = re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))", line)
            start_digit = subs.get(digits[0], digits[0])
            end_digit = subs.get(digits[-1], digits[-1])
            total += int(f"{start_digit}{end_digit}")
        print(total)

