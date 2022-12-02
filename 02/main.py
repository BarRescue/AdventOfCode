# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def part_one():
    file = open('input', 'r')
    lines = file.readlines()
    part_one_score = 0
    part_two_score = 0

    for line in lines:
        choices = line.split()

        opponent_hand = "ABC".index(choices[0]) + 1
        own_hand = "XYZ".index(choices[1]) + 1

        part_one_score += (calculate_win_part_one(own_hand, opponent_hand) + own_hand)
        part_two_score += calculate_win_part_two(own_hand, opponent_hand)

    print(part_one_score)
    print(part_two_score)


def calculate_win_part_two(own, opponent):
    if own == 2:
        if opponent == 1:
            return 4
        if opponent == 2:
            return 5
        if opponent == 3:
            return 6

    if own == 1:
        if opponent == 1:
            return 3
        if opponent == 2:
            return 1
        if opponent == 3:
            return 2

    if own == 3:
        if opponent == 1:
            return 8
        if opponent == 2:
            return 9
        if opponent == 3:
            return 7


def calculate_win_part_one(own, opponent):
    if opponent == 1 and own == 2 or opponent == 2 and own == 3 or opponent == 3 and own == 1:
        return 6
    if opponent == 1 and own == 1 or opponent == 2 and own == 2 or opponent == 3 and own == 3:
        return 3
    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_one()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
