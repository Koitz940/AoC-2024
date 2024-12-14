import importlib
from time import time

day = input("select a day:\n[1] day 1\n[2] day 2\n...\n")
if day.isnumeric():
    if "." in day:
        print("a day is an int, not a float")
        exit(1)
    if "j" in day:
        print("a day is an int, not a complex")
        exit(1)
    if "-" in day:
        print("a negative day? really? I mean I wish we had problems since idk November 1st but that's not the case")
        exit(1)
    if "+" in day:
        print("...")
        print("fine, that technically works, but my only question is why you added the + sign")
        exit(1)
else:
    print("a number, plz")
    exit(1)

day = int(day)

try:
    mod = importlib.import_module("day" + str(day))
    part = input("select a part:\n[1] part 1\n[2] part 2\n")
    if part.isnumeric():
        if "." in part:
            print("a day is an int, not a float")
            exit(1)
        if "j" in part:
            print("a day is an int, not a complex")
            exit(1)
        if "-" in part:
            print(
                "a negative day? really? I mean I wish we had problems since idk November 1st but that's not the case")
            exit(1)
        if "+" in part:
            print("...")
            print("fine, that technically works, but my only question is why you added the + sign")
            exit(1)
    else:
        print("a number, plz")
        exit(1)
    try:
        f = getattr(mod, "part" + str(part))
        try:
            file = input("insert file name: ")
            if not file:
                file = f"files/day{day}_file"
            start = time()
            solution = f(file)
            end = time()
            print(f"The solution to part {part} of day {day} for the file named {file} is {solution}, which took {end - start}s")
        except FileNotFoundError:
            print("file not found")
            exit(1)

    except ValueError:
        print("AoC has part 1 and part 2")

except ModuleNotFoundError:
    if 1 <= day <= 25:
        print("day not supported yet")
        exit(1)
    else:
        print("the range of days is 1-25")
        exit(1)
