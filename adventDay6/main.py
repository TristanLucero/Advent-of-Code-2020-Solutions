#Advent of code 2020 Day 4
import string

def main():
    with open('f.txt') as f:
        content = f.read()
    content = content.split("\n\n")

    #part 1
    # content = [temp.replace('\n', '') for temp in content]
    # total = 0
    # for group in content:
    #     myDict = {}
    #     for letter in group:
    #         if letter not in myDict:
    #             myDict[letter] = 1
    #     total += len(myDict)
    # print(total)

    #part 2
    content = [temp.replace('\n', ' ') for temp in content]
    total = 0
    for group in content:
        myDict = {}
        group = group.split(" ")
        for letter in string.ascii_lowercase:
            if all([letter in c for c in group]):
                if letter not in myDict:
                    myDict[letter] = 1
        total += len(myDict)
    print(total)


if __name__ == '__main__':
    main()