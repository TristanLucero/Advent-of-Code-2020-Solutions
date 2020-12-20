# Advent Day 11 Part 1 & 2

import copy

def how_many_adjacent_occupants(v, x, y):
    total = 0
    offsets = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for d in offsets:
        dx = x + d[0]
        dy = y + d[1]
        while dy >= 0 and dy < len(v) and dx >= 0 and dx < len(v[dy]) and v[dy][dx] == '.':
            dx += d[0]
            dy += d[1]
        if dy >= 0 and dy < len(v) and dx >= 0 and dx < len(v[dy]):
            total += (v[dy][dx] == "#")
    return total

def get_total_occupants(v):
    total = 0
    for x in v:
        total += x.count("#")
    return total

def main():
    with open('f.txt') as f:
        content = f.read().split("\n")


    # # Part 1
    # content = [list(x) for x in content]
    # nextRound = copy.deepcopy(content) #[x[:] for x in content]
    # i = 0
    # while 1:
    #     content = copy.deepcopy(nextRound)
    #     # row
    #     for i in range(len(content)):
    #         # seat
    #         for j in range(len(content[i])):
    #             n = [0, 0, 0, 0, 0, 0, 0, 0]
    #             top = i - 1
    #             bottom = i + 1
    #             left = j - 1
    #             right = j + 1
    #             if top >= 0 and left >= 0:
    #                 n[0] = content[top][left]
    #             if top >= 0:
    #                 n[1] = content[top][j]
    #             if top >= 0 and right <= len(content[i]) - 1:
    #                 n[2] = content[top][right]
    #             if left >= 0:
    #                 n[3] = content[i][left]
    #             if right <= len(content[i]) - 1:
    #                 n[4] = content[i][right]
    #             if bottom <= len(content) - 1 and left >= 0:
    #                 n[5] = content[bottom][left]
    #             if bottom <= len(content) - 1:
    #                 n[6] = content[bottom][j]
    #             if bottom <= len(content) - 1 and right <= len(content[i]) - 1:
    #                 n[7] = content[bottom][right]
    #             if content[i][j] == "L" and n.count("#") == 0:
    #                 nextRound[i][j] = "#"
    #             if content[i][j] == "#" and n.count("#") >= 4:
    #                 nextRound[i][j] = "L"
    #     if content == nextRound:
    #         break
    # # Prints number of # in nextRound
    # print(sum([x.count("#") for x in nextRound]))

    # Part 2
    for generations in range(100):
        next = []
        a = 0
        for y in range(len(content)):
            string = ""
            for x in range(len(content[y])):
                a += 1
                character = content[y][x]
                if character != '.':
                    occupants = how_many_adjacent_occupants(content, x, y)
                    if character == "L" and occupants == 0:
                        character = "#"
                    elif character == "#" and occupants >= 5:
                        character = "L"
                string += character
            next.append(string)
        content = next
    print("PART 2 SOLUTION: " + str(get_total_occupants(content)))




if __name__ == '__main__':
    main()
