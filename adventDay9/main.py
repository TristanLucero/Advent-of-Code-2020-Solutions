# Advent Day 9
def main():
    with open('f.txt') as f:
        content = f.read()
    content = [int(x) for x in content.split("\n")]

    # Part 1
    preambleList = []
    preambleLen = 25
    for i in range(preambleLen):
        preambleList.append(content[i])

    for i in range(preambleLen, len(content) - 1):
        for j in range(len(preambleList) - 1):
            for k in range(j + 1, len(preambleList)):
                if preambleList[j] + preambleList[k] == content[i]:
                    break
            else:
                continue
            break
        else:
            print("Number to check: ", content[i])
            numToCheck = content[i]

            break
        del preambleList[0]
        preambleList.append(content[i])

    # Part 2
    for i in range(len(content)):
        tmpNum = 0
        tmpNum = content[i]
        for j in range(i + 1, len(content)):
            tmpNum += content[j]
            if tmpNum == numToCheck:
                myList = content[i:j+1]
                myList.sort()
                print(myList[0] + myList[-1])
                exit()
            if tmpNum > numToCheck:
                break


if __name__ == '__main__':
    main()
