# Advent Day 10
def main():
    with open('f.txt') as f:
        content = f.read()
    content = [int(x) for x in content.split("\n")]
    print(content)

    # Part 1
    # content.sort()
    # deviceJ = max(content) + 3
    # zeroJoltDiff = 0
    # oneJoltDiff = 0
    # twoJoltDiff = 0
    # threeJoltDiff = 0
    #
    # for i in range(len(content)):
    #     contentMin = content[0]
    #     if i == 0:
    #         step = contentMin - 0
    #     else:
    #         nextAdapt = content[1]
    #         content.remove(contentMin)
    #         step = nextAdapt - contentMin
    #     if step == 0:
    #         zeroJoltDiff += 1
    #     elif step == 1:
    #         oneJoltDiff += 1
    #     elif step == 2:
    #         twoJoltDiff += 1
    #     elif step == 3:
    #         threeJoltDiff += 1
    # threeJoltDiff += 1
    # print(zeroJoltDiff, oneJoltDiff, twoJoltDiff, threeJoltDiff)
    # print("1-jolt diff * 3-jolt diff: ", oneJoltDiff*threeJoltDiff)

    # Part 2
    content.append(0)
    content.append(max(content) + 3)
    content.sort()
    print(content)

    paths = [0] * (max(content) + 1)
    paths[0] = 1

    for i in range(1, max(content) + 1):
        for j in range(1, 4):
            if i - j in content:
                paths[i] += paths[i - j]
    print(paths[-1])


if __name__ == '__main__':
    main()
