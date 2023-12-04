def day4p1():
    f = open("day4/data.txt", "r")
    lines = f.readlines()
    f.close()

    example = [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]

    total = 0
    for line in lines:
        line = line[10:]
        winning_numbers = line.split(" | ")[0]
        winning_numbers = winning_numbers.split(" ")
        numbers = line.split(" | ")[1]
        numbers = numbers.split(" ")
        
        for number in winning_numbers:
            if number == "":
                winning_numbers.remove(number)
        for number in numbers:
            if number == "":
                numbers.remove(number)

        print(line[:10])
        points = 0
        for number in numbers:
            print("Checking " + number)
            if number in winning_numbers:
                print("Matched " + number)
                if points == 0:
                    points = 1
                else:
                    points *= 2
        total += points
            

    print(total)

def day4p2():
    return 0