#Advent of code 2020 Day 3
import functools


def main():
    with open('f.txt') as f:
        content = f.readlines()

    print("Part 1 solution: ", find_tree(3, 1, content))
    solList = [find_tree(1, 1, content),
    find_tree(3, 1, content),
    find_tree(5, 1, content),
    find_tree(7, 1, content),
    find_tree(1, 2, content)]

    #to multiply solList
    print("Part 2 solution: ", functools.reduce(lambda a, b: a*b, solList))

#What the lambda function does
# def mul(a, b):
#     return a*b


def find_tree(xStep, yStep, content):
    content2 = []
    for i in content:
        # strip is to remove newline character when duplicating
        content2.append(i.strip() * len(content) * 3)

    tree = '#'
    treeCount = 0
    xIndex = 0
    yIndex = 0

    while yIndex < len(content):
        if list(content2[yIndex])[xIndex] == tree:
            treeCount += 1
        xIndex += xStep
        yIndex += yStep
    return treeCount


if __name__ == '__main__':
    main()