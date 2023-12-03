from operator import itemgetter
import re

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

    for line in data:
        regexFirst = re.compile(r'(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)')
        regexLast = re.compile(r'(eno)|(owt)|(eerht)|(ruof)|(evif)|(xis)|(neves)|(thgie)|(enin)|(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)')

        first = re.search(regexFirst, line)
        last = re.search(regexLast, line[::-1])
        number = str(numbers[first.group()]) + str(numbers[last.group()[::-1]])
        print(line + " ==> " + number)
        total += int(number)

    print(total)