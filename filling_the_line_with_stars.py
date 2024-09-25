# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors.
# A tower block is represented with "*" character.
#
# For example, a tower with 3 floors looks like this:
#
# [
#   "  *  ",
#   " *** ",
#   "*****"
# ]


def tower_builder(floors):
    tower = []
    for i in range(floors):
        spaces = " " * (floors - i - 1)
        blocks = "*" * (2*i + 1)
        tower.append(spaces + blocks + spaces)
    return tower

print(tower_builder(3))
