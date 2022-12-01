# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def solve_puzzle():
    file = open('input', 'r')
    lines = file.readlines()

    calories_counted = 0
    calories = []

    for line in lines:
        if line.strip() == "":
            calories.append(calories_counted)
            calories_counted = 0
        else:
            calories_counted += int(line.strip())

    calories.sort(reverse=True)

    # Part one
    print(calories[0])

    # Part two
    three_elves = 0
    for index in range(3):
        three_elves += calories[index]

    print(three_elves)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solve_puzzle()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
