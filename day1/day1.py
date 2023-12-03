from operator import itemgetter

def day1p1():
    file = open("day1/data.txt", "r")
    data = file.readlines()
    file.close()

    total = 0 
    # for each line in the data
    for line in data:
        first = ""
        second = ""

        # find the first number and return it
        for letter in line:
            if (letter.isnumeric()):
                second = letter

        for letter in line[::-1]:
            if (letter.isnumeric()):
                first = letter

        print(first + second)
        number = int(first + second)
        total += number
    
    print(total)

def day1p2():
    file = open("day1/data.txt", "r")
    data = file.readlines()
    file.close()

    total = 0
    numbers = { 
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6" : 6, "7": 7, "8": 8, "9": 9            
    }

    for line in ["two934seven1", "sgoneightfoureight5sevenjzsqghg"]:
        tokens = []

        for letter in line:
            if letter.isnumeric():
                tokens.append([letter, line.index(letter)]);

        for letter in line:
            for number in numbers:
                substring = line[line.index(letter):line.index(letter) + len(number)]
                print(substring, number)
                if substring == number:
                    tokens.append(number)
        
        print(line, tokens)

    print(total)