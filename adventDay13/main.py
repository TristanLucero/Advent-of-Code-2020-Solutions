# Advent of code day 13
# Part 1 and 2

from math import gcd


def leastCommonFactor(arr):
    lcm = arr[0][0]
    for num in arr[1:]:
        lcm = (lcm * num[0]) // gcd(lcm, num[0])
    return lcm


def main():
    with open('f.txt') as f:
        content = f.read()
    content = content.split("\n")

    # Part 1
    # earliestTime = int(content[0])
    # time = int(content[0])
    # busses = [int(x) for x in content[1].split(",") if x != "x"]
    #
    # foundBus = False
    # while not foundBus:
    #     for bus in busses:
    #         if time % bus == 0:
    #             foundBus = True
    #             foundBusID = bus
    #             break
    #         else:
    #             time += 1
    # print((time - earliestTime) * foundBusID)

    busses  = []
    count = 0
    for bus in content[1].split(","):
        if bus != "x":
            busses.append([int(bus), count])
        count += 1
    busses.sort()
    print(busses)

    time = 1 # starting time
    time_to_add = 1
    for i in range(1, len(busses)):
        lineGood = False
        while not lineGood:
            lineGood = True
            # first check that first 2 busses are good
            # then will break into above for
            # then this loop will check first 3
            # then break again, etc.
            # + 1 is not included, just goes till i basically.
            for j in range(0, i + 1):
                if (time + busses[j][1]) % busses[j][0] != 0:
                    lineGood = False
                    break
            if lineGood:
                time_to_add = leastCommonFactor(busses[:j])
            else:
                time += time_to_add
    print(time)


if __name__ == '__main__':
    main()
