#Advent of code 2020 Day 1 Part 1+2
def main():
    with open('myFile.txt') as f:
        content = [int(var) for var in f.read().split('\n')]

    num = 2020
    myHash = {}
    for i in range(len(content)):
        myHash[content[i]] = i

    #Part 1
    for i in range(len(content)):
        inverse = num - content[i]
        if inverse in myHash:
            print([content[i], content[myHash[inverse]]])
            print([content[i] * content[myHash[inverse]]])
            exit()

    # Part 2
    # for i in range(len(content)):
    #     for j in range(len(content[i + 1:])):
    #         inverse = num - content[i] - content[j]
    #         if inverse in myHash:
    #             print([content[i], content[j], content[myHash[inverse]]])
    #             print([content[i] * content[j] * content[myHash[inverse]]])
    #             exit()


if __name__ == '__main__':
    main()
