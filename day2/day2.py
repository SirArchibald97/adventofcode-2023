def day2p1():
    f = open("day2/data.txt", "r")
    lines = f.readlines()
    f.close()

    total = 0
    # 12 green, 13 blue, 14 red
    for line in lines:
        id = line.split(":")[0].split(" ")[1]
        possible = True

        print("==[ " + id + " ]==")
        for set in line.split(":")[1].strip().split("; "):
            colours = set.split(", ")
            
            for colour in colours:
                if "green" in colour:
                    amount = int(colour.split(" ")[0])
                    if amount > 13:
                        possible = False
                        print(" - " + colour + " ❌ ")
                    else:
                        print(" - " + colour + " ✅ ")
                
                elif "blue" in colour:
                    amount = int(colour.split(" ")[0])
                    if amount > 14:
                        possible = False
                        print(" - " + colour + " ❌ ")
                    else:
                        print(" - " + colour + " ✅ ")

                elif "red" in colour:
                    amount = int(colour.split(" ")[0])
                    if amount > 12:
                        possible = False
                        print(" - " + colour + " ❌ ")
                    else:
                        print(" - " + colour + " ✅ ")

            print(" = " + str(possible) + "\n-------")
                
        if possible:
            total += int(id)
        
    print(total)
            

def day2p2():
    f = open("day2/data.txt", "r")
    lines = f.readlines()
    f.close()

    total = 0
    for line in lines:
        # red, green, blue
        smallest = [0, 0, 0]

        print(line)
        for set in line.split(":")[1].strip().split("; "):
            colours = set.split(", ")
            for colour in colours:
                if "red" in colour:
                    amount = int(colour.split(" ")[0])
                    if amount > smallest[0]:
                        smallest[0] = amount
                elif "green" in colour:
                    amount = int(colour.split(" ")[0])
                    if amount > smallest[1]:
                        smallest[1] = amount
                elif "blue" in colour:
                    amount = int(colour.split(" ")[0])
                    if amount > smallest[2]:
                        smallest[2] = amount
            print(smallest)

        power = smallest[0] * smallest[1] * smallest[2]
        total += power

    print(total)