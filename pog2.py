import random

loop = True
while loop is True:
    unit_type = input("army, corps(c) or flanking check(f)?")
    if unit_type == "c":
        print(
            "How many factors firing(after column shift for trench, swamp, mountains)?"
        )
        column = int(input("Which column(between 1 and 8)?"))
        drm = int(input("Any dice rolls modifiers?"))
        roll = random.randint(0, 5)
        modified_roll = roll + int(drm)
        if modified_roll > 5:
            modified_roll = 5
        elif modified_roll < 0:
            modified_roll = 0
        print(f"Roll (after modifiers): {modified_roll}")
        columns = [
            {0: [0, 0, 0, 0, 1, 1]},
            {1: [0, 0, 0, 1, 1, 1]},
            {2: [0, 1, 1, 1, 1, 1]},
            {3: [1, 1, 1, 1, 2, 2]},
            {4: [1, 1, 1, 2, 2, 2]},
            {5: [1, 1, 2, 2, 2, 3]},
            {6: [1, 1, 2, 2, 3, 3]},
            {7: [1, 2, 2, 3, 3, 4]},
            {8: [2, 2, 3, 3, 4, 4]},
        ]
        result = columns[column][column][modified_roll]
        print(f"Table result: {result}")
    elif unit_type == "f":
        flanking_hexes = int(input("How many flanking hexes(not including pinning hex)?"))
        roll = random.randint(0, 5) + flanking_hexes
        if roll >= 3:
            print("Flanking successful!")
        else:
            print("Flanking unsuccessful!")
    else:
        print(
            "How many factors firing(after column shift for trench, swamp, mountains)?"
        )
        column = int(input("Which column (between 1 and 16)?"))
        drm = int(input("Any dice rolls modifiers?"))
        roll = random.randint(0, 5)
        modified_roll = roll + int(drm)
        if modified_roll > 5:
            modified_roll = 5
        elif modified_roll < 0:
            modified_roll = 0
        print(f"Roll (after modifiers): {modified_roll}")
        columns = [
            {0: [1, 1]},
            {1: [0, 1, 1, 1, 2, 2]},
            {2: [1, 1, 2, 2, 3, 3]},
            {3: [1, 2, 2, 3, 3, 4]},
            {4: [2, 2, 3, 3, 4, 4]},
            {5: [2, 3, 3, 4, 4, 5]},
            {6: [3, 3, 4, 4, 5, 5]},
            {7: [3, 3, 4, 4, 5, 5]},
            {8: [3, 3, 4, 4, 5, 5]},
            {9: [3, 4, 4, 5, 5, 7]},
            {10: [3, 4, 4, 5, 5, 7]},
            {11: [3, 4, 4, 5, 5, 7]},
            {12: [4, 4, 5, 5, 7, 7]},
            {13: [4, 4, 5, 5, 7, 7]},
            {14: [4, 4, 5, 5, 7, 7]},
            {15: [4, 5, 5, 7, 7, 7]},
            {16: [5, 5, 7, 7, 7, 7]},
        ]
        result = columns[column][column][modified_roll]
        print(f"Table result: {result}")
