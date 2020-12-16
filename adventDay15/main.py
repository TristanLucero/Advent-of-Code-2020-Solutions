# Advent of code day 15
# Part 1 and 2

def main():
    with open('f.txt') as f:
        content = f.read()

    # Part 1 & 2
    content = [int(x) for x in content.split(",")]
    prevSpokenDict = {}
    for i in range(len(content)):
        if i != len(content) - 1:
            prevSpokenDict[content[i]] = i + 1
        lastSpoken = content[i]
    for i in range(len(content), 30000000): # change to 2020 for part 1
        if lastSpoken not in prevSpokenDict:
            prevSpokenDict[lastSpoken] = i
            lastSpoken = 0
        else:
            tmp = i - prevSpokenDict[lastSpoken]
            prevSpokenDict[lastSpoken] = i
            lastSpoken = tmp
    print(lastSpoken)


if __name__ == '__main__':
    main()
