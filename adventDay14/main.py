# Advent of code day 14
# Part 1 and 2
to_bin = lambda n, size: "".join([str(int((2 ** i) & n and 1)) for i in range(size)])[::-1]


def main():
    with open('f.txt') as f:
        content = f.read()

    # # Part 1
    # memDict = {}
    # for line in content.split("\n"):
    #     lineArr = line.split(" = ")
    #     if lineArr[0] == "mask":
    #         mask = lineArr[1]
    #     else:
    #         memNum = int(lineArr[0].replace("mem[", "").replace("]", ""))
    #         binValue = list(to_bin(int(lineArr[1]), 36))
    #         for i in range(len(mask)):
    #             if mask[i] == "1":
    #                 binValue[i] = "1"
    #             elif mask[i] == "0":
    #                 binValue[i] = "0"
    #         memDict[memNum] = int("".join(binValue), 2)
    # print("Final bin: ", sum(memDict.values()))

    # Part 2
    memDict = {}
    for line in content.split("\n"):
        lineArr = line.split(" = ")
        if lineArr[0] == "mask":
            mask = lineArr[1]
        else:
            xList = []
            memNum = int(lineArr[0].replace("mem[", "").replace("]", ""))
            binValueOfMem = list(to_bin(memNum, 36))
            for i in range(len(mask)):
                if mask[i] == "1":
                    binValueOfMem[i] = "1"
                elif mask[i] == "X":
                    xList.append(i)
            for i in range(2 ** len(xList)):
                binCount = to_bin((int(i-1) + 1), len(xList))
                for j in range(len(binCount)):
                    binValueOfMem[xList[j]] = binCount[j]
                memDict[int("".join(binValueOfMem), 2)] = int(lineArr[1])
    print("Final bin: ", sum(memDict.values()))


if __name__ == '__main__':
    main()
