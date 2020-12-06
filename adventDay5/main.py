#Advent of code 2020 Day 5
def main():
    with open('f.txt') as f:
        content = f.read()
    seatList = content.split("\n")
    highestSeat = 0
    seatIDList = []

    for line in seatList:
        bottomRange = 0
        topRange = 127
        rightRange = 0
        leftRange = 7
        for i in range(7):
            if line[i] == "F":
                topRange = topRange - round((topRange-bottomRange) / 2)
                finalRow = bottomRange
            elif line[i] == "B":
                bottomRange = bottomRange + round((topRange - bottomRange) / 2)
                finalRow = topRange
        for i in range(7, 10):
            if line[i] == "L":
                leftRange = leftRange - round((leftRange-rightRange) / 2)
                finalCol = rightRange
            elif line[i] == "R":
                rightRange = rightRange + round((leftRange - rightRange) / 2)
                finalCol = leftRange
        seatID = finalRow * 8 + finalCol
        seatIDList.append(seatID)
        if seatID > highestSeat:
            highestSeat = seatID

    seatIDList.sort()
    sumOfNums = 0
    startNum = seatIDList[0]
    endNum = seatIDList[len(seatIDList) - 1] + 1
    for i in range(startNum, endNum):
        sumOfNums += i
    print(sumOfNums - sum(seatIDList))
    print(highestSeat)

if __name__ == '__main__':
    main()