#Advent Day 8
def main():
    with open('f.txt') as f:
        content = f.read()
    content = content.split("\n")

    # Part 1
    # visited = {}
    # accCount = 0
    # currLine = 0
    # while currLine < len(content):
    #     ins, num = content[currLine].split(" ")
    #     num = int(num)
    #     if currLine not in visited:
    #         visited[currLine] = 1
    #     else:
    #         break
    #
    #     if ins == "acc":
    #         accCount += num
    #     if ins == "jmp":
    #         currLine += num
    #     else:
    #         currLine += 1
    # print(accCount)

    # Part 2
    currLine = 0
    while currLine < len(content):
        ins, num = content[currLine].split(" ")
        num = int(num)
        if ins != "acc":
            tmpContent = content[:]
            if ins == "nop":
                tmpContent[currLine] = "jmp" + content[currLine][3:]
            if ins == "jmp":
                tmpContent[currLine] = "nop" + content[currLine][3:]
            if exe_code(tmpContent):
                break
        currLine += 1
    print(exe_code(tmpContent))


def exe_code(content):
    visited = {}
    accCount = 0
    currLine = 0
    while currLine < len(content):
        ins, num = content[currLine].split(" ")
        num = int(num)
        if currLine not in visited:
            visited[currLine] = 1
        else:
            return False

        if ins == "acc":
            accCount += num
        if ins == "jmp":
            currLine += num
        else:
            currLine += 1
    return accCount


if __name__ == '__main__':
    main()
