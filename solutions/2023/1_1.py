import re

if __name__ == "__main__":
    total = 0
    with open("../../data/2023/1_1.txt") as f:
        for line in f:
            digits = re.sub("[^0-9]", "", line)
            total += int(f"{digits[0]}{digits[-1]}")
    print(total)
