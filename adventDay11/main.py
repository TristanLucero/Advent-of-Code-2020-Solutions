import copy

def main():
    with open('f.txt') as f:
        content = f.read()
    content = content.split("\n")
    content = [list(x) for x in content]

    # # Part 1
    nextRound = copy.deepcopy(content) #[x[:] for x in content]
    i = 0
    while 1:
        content = copy.deepcopy(nextRound)
        # row
        for i in range(len(content)):
            # seat
            for j in range(len(content[i])):
                n = [0, 0, 0, 0, 0, 0, 0, 0]
                top = i - 1
                bottom = i + 1
                left = j - 1
                right = j + 1
                if top >= 0 and left >= 0:
                    n[0] = content[top][left]
                if top >= 0:
                    n[1] = content[top][j]
                if top >= 0 and right <= len(content[i]) - 1:
                    n[2] = content[top][right]
                if left >= 0:
                    n[3] = content[i][left]
                if right <= len(content[i]) - 1:
                    n[4] = content[i][right]
                if bottom <= len(content) - 1 and left >= 0:
                    n[5] = content[bottom][left]
                if bottom <= len(content) - 1:
                    n[6] = content[bottom][j]
                if bottom <= len(content) - 1 and right <= len(content[i]) - 1:
                    n[7] = content[bottom][right]
                if content[i][j] == "L" and n.count("#") == 0:
                    nextRound[i][j] = "#"
                if content[i][j] == "#" and n.count("#") >= 4:
                    nextRound[i][j] = "L"
        if content == nextRound:
            break
    #print(nextRound)

    # Prints number of # in nextRound
    print(sum([x.count("#") for x in nextRound]))


if __name__ == '__main__':
    main()
