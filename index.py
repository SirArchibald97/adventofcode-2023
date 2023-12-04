import day1.day1 as day1
import day2.day2 as day2

import day4.day4 as day4

day = input("Enter a day (1-24): ")
part = input("Enter a part (1-2): ")

days = {
    "1-1": getattr(day1, "day1p1"),
    "1-2": getattr(day1, "day1p2"),
    "2-1": getattr(day2, "day2p1"),
    "2-2": getattr(day2, "day2p2"),


    "4-1": getattr(day4, "day4p1"),
    "4-2": getattr(day4, "day4p2"),
}

if (day + "-" + part) in days:
    days[day + "-" + part]()
else:
    print("I do not have a solution for that day yet!")