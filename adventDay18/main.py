# Advent of code day 18
# Part 1 and 2

# Part 1
# def process_problem(sub_list):
#     solution = int(sub_list[0])
#     for i in range(2, len(sub_list), 2):
#         if sub_list[i - 1] == "+":
#             solution += int(sub_list[i])
#         elif sub_list[i - 1] == "*":
#             solution *= int(sub_list[i])
#     return solution


# Part 2
def process_problem(sub_list):
    # This while loop does all addition first
    z = 2
    while 1:
        if sub_list[z - 1] == "+":
            sub_list = sub_list[0:z-2:] + [int(sub_list[z - 2]) + int(sub_list[z])] + sub_list[z+1::]
            z = 0
        z += 2
        if z > len(sub_list):
            break

    # Same as part 1, does multiplication / addition
    solution = int(sub_list[0])
    for i in range(2, len(sub_list), 2):
        if sub_list[i - 1] == "+":
            solution += int(sub_list[i])
        elif sub_list[i - 1] == "*":
            solution *= int(sub_list[i])
    return solution


def main():
    with open('f.txt') as f:
        content = f.read()
    content = content.split("\n")

    contentSolution = 0
    for line in content:
        lineList = list("(" + line.replace(" ", "") + ")")
        parenStack = []
        # init while loop
        i = 0
        while 1:
            if lineList[i] == "(":
                parenStack.append(i)
            elif lineList[i] == ")":
                leftParenLocation = parenStack.pop()
                rightParenLocation = i
                lineList = lineList[0:leftParenLocation:] + [
                    process_problem(lineList[leftParenLocation + 1:rightParenLocation:])] + lineList[
                                                                                            rightParenLocation + 1::]
                if parenStack:
                    i = parenStack[-1] + 1
            if len(lineList) == 1:
                contentSolution += lineList[0]
                break
            i += 1
    print("Content solution: ", contentSolution)


if __name__ == '__main__':
    main()
