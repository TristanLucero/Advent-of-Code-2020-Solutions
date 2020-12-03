#Advent of code 2020 Day 2

def main():
    with open('f.txt') as f:
        content = f.readlines()

    content2 = []
    for i in content:
        content2.append(i.split(" "))

    #PART 1
    # validCount = 0
    # letterCount = 0
    # for i in range(len(content)):
    #     lowNum = int(content2[i][0].split("-")[0])
    #     highNum = int(content2[i][0].split("-")[1])
    #     letter = list(content2[i][1])[0]
    #
    #     for j in list(content2[i][2]):
    #         if j == letter:
    #             letterCount += 1
    #     if lowNum <= letterCount <= highNum:
    #         validCount += 1
    #     letterCount = 0
    # print(validCount)


    #PART 2
    validCount = 0
    letterCount = 0
    for i in range(len(content)):
        lowNum = int(content2[i][0].split("-")[0])-1
        highNum = int(content2[i][0].split("-")[1])-1
        letter = list(content2[i][1])[0]
        if list(content2[i][2])[lowNum] == letter and list(content2[i][2])[highNum] != letter or list(content2[i][2])[highNum] == letter and list(content2[i][2])[lowNum] != letter:
            validCount += 1
    print(validCount)

if __name__ == '__main__':
    main()