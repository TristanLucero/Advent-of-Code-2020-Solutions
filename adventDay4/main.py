#Advent of code 2020 Day 4
def main():
    with open('f.txt') as f:
        content = f.read()
    content = content.split("\n\n")
    content = [temp.replace('\n', ' ') for temp in content]
    requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    #Part 1 good solution
    # validPassCount = 0
    # for passport in content:
    #     fields = passport.split(" ")
    #     valid = 0
    #     for j in fields:
    #         field = j.split(":")[0]
    #         valid |= 1 << requiredFields.index(field) if field in requiredFields else 0
    #
    #     if valid == 0x7F:
    #         validPassCount += 1
    # print(validPassCount)

    #Part 2 (not that great of a solution solution)
    validPassCount = 0
    for passport in content:
        validFields = [0, 0, 0, 0, 0, 0, 0]
        fields = passport.split(" ")
        valid = 0
        for j in range(len(fields)):
            field = fields[j].split(":")[0]
            fieldVal = fields[j].split(":")[1]
            if field == requiredFields[0] and 1920 <= int(fieldVal) <= 2002:
                validFields[0] = 1
            elif field == requiredFields[1] and 2010 <= int(fieldVal) <= 2020:
                validFields[1] = 1
            elif field == requiredFields[2] and 2020 <= int(fieldVal) <= 2030:
                validFields[2] = 1
            elif field == requiredFields[3] and fieldVal.endswith("cm") or fieldVal.endswith("in"):
                if fieldVal.endswith("cm"):
                    fieldVal = fieldVal.replace("cm", "")
                    if 150 <= int(fieldVal) <= 193:
                        validFields[3] = 1
                elif fieldVal.endswith("in"):
                    fieldVal = fieldVal.replace("in", "")
                    if 59 <= int(fieldVal) <= 76:
                        validFields[3] = 1
            elif field == requiredFields[4] and fieldVal.startswith("#"):
                fieldVal = fieldVal.replace("#", "")
                if [x for x in fieldVal if x.isdigit() and 0 <= int(x) <= 9 or x in "abcdef"]:
                    validFields[4] = 1
            elif field == requiredFields[5] and fieldVal == "amb" or fieldVal == "blu" or fieldVal == "brn" or fieldVal == "gry" or fieldVal == "grn" or fieldVal == "hzl" or fieldVal == "oth":
                validFields[5] = 1
            elif field == requiredFields[6] and fieldVal.isdigit() and len(fieldVal) == 9:
                validFields[6] = 1
        if sum(validFields) == 7:
            validPassCount += 1
        del validFields[:]
    print(validPassCount)


if __name__ == '__main__':
    main()
