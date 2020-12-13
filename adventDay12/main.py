import copy

def main():
    with open('f.txt') as f:
        content = f.read()
    content = content.split("\n")
    content = [[x[0], int(x[1:])] for x in content]

    # #NESW
    # # N = 0
    # # E = 1
    # # S = 2
    # # W = 3
    # direction = 1
    # eastPos = 0
    # northPos = 0
    # for line in content:
    #     ins = line[0]
    #     num = line[1]
    #     if ins == "N":
    #         northPos += num
    #     elif ins == "S":
    #         northPos -= num
    #     elif ins == "E":
    #         eastPos += num
    #     elif ins == "W":
    #         eastPos -= num
    #     elif ins == "L":
    #         if num % 360 == 0:
    #             direction = (direction - 0) % 4
    #         elif num % 360 == 90:
    #             direction = (direction - 1) % 4
    #         elif num % 360 == 180:
    #             direction = (direction - 2) % 4
    #         elif num % 360 == 270:
    #             direction = (direction - 3) % 4
    #     elif ins == "R":
    #         if num % 360 == 0:
    #             direction = (direction + 0) % 4
    #         elif num % 360 == 90:
    #             direction = (direction + 1) % 4
    #         elif num % 360 == 180:
    #             direction = (direction + 2) % 4
    #         elif num % 360 == 270:
    #             direction = (direction + 3) % 4
    #     elif ins == "F":
    #         if direction == 0:
    #             northPos += num
    #         elif direction == 1:
    #             eastPos += num
    #         elif direction == 2:
    #             northPos -= num
    #         elif direction == 3:
    #             eastPos -= num
    # print("Direction: ", direction)
    # print("East Pos: ", eastPos, "North Pos: ", northPos)
    # print(abs(eastPos) + abs(northPos))


    # Part 2
    #NESW
    # N = 0
    # E = 1
    # S = 2
    # W = 3
    direction = 1
    eastPos = 0
    northPos = 0
    waypointEastPos = 10
    waypointNorthPos = 1
    waypointDirection = 1
    for line in content:
        ins = line[0]
        num = line[1]
        if ins == "N":
            waypointNorthPos += num
        elif ins == "S":
            waypointNorthPos -= num
        elif ins == "E":
            waypointEastPos += num
        elif ins == "W":
            waypointEastPos -= num
        elif ins == "L":
            for i in range((num // 90) % 4):
                temp = waypointNorthPos
                waypointNorthPos = waypointEastPos
                waypointEastPos = -temp
        elif ins == "R":
            for i in range((num // 90) % 4):
                temp = waypointNorthPos
                waypointNorthPos = -waypointEastPos
                waypointEastPos = temp
        elif ins == "F":
            eastPos += waypointEastPos * num
            northPos += waypointNorthPos * num

    print("Direction: ", direction)
    print("East Pos: ", eastPos, "North Pos: ", northPos)
    print("Manhattan distance: ", abs(eastPos) + abs(northPos))


if __name__ == '__main__':
    main()
