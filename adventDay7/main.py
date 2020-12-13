def main():
    # have bagDict for all bags
    # if bag not in bagDict, add to bagDict
    # bag is key, lookup is list of bags that the bag can hold

    with open('f.txt') as f:
        content = f.read()
    content = content.replace(" contain", ",")
    content = content.replace(".", "")
    content = content.replace("bags", "bag")
    content = content.replace(" bag", "")
    content = content.split("\n")

    bagDict = {}
    for bag in content:
        bagList = bag.split(", ")
        bagSubDict = {}
        [bagSubDict.update([[z[1] if z[1] != "other" else "", int(z[0]) if z[0].isdigit() else 0]]) for z in
         [x.split(" ", 1) for x in bagList[1:]]]
        bagDict[bagList[0]] = bagSubDict
    # Part 1
    # shinyCount = 0
    # # variable we're first searching for is :shiny gold"
    # toCheckQueue = ["shiny gold"]
    # checkedSet = set()
    # while toCheckQueue:
    #     # pop queue and get next variable to search for
    #     searchVar = toCheckQueue.pop(0)
    #     # add variable to checked set
    #     checkedSet.add(searchVar)
    #     # this is for key, value in bagDict.items()
    #     for bag, subBags in bagDict.items():
    #         if searchVar in subBags and not bag in checkedSet:
    #             toCheckQueue.append(bag)
    #             # checkedBagCountSet += subBags[searchVar]
    # print(len(checkedSet) - 1)

    # Part 2
    print(count_bags(bagDict, "shiny gold") - 1)


def count_bags(bagDict, container):
    a = 0
    if bagDict and container in bagDict:
        for subBag in bagDict[container]:
            a += bagDict[container][subBag] * count_bags(bagDict, subBag)
        a += 1
    return a


if __name__ == '__main__':
    main()
