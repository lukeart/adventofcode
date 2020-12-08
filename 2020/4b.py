
def main():

    file1 = open('./4.lk.in', 'r')
    lines = file1.read()
    counter = 0
    passports = lines.split("\n\n")
    for p in passports:
        valid = True
        elements = p.replace('\n', ' ').split()

        filtered_elements = list(filter(lambda e: "cid:" not in e, elements))
        # print(len(filtered_elements))
        if len(filtered_elements) < 7:
            continue
        for e in filtered_elements:
            print(e)
            field, val = e.split(':')
            if field == "byr":
                valid &= int(val) >= 1920 and int(val) <= 2002
            if field == "iyr":
                valid &= int(val) >= 2010 and int(val) <= 2020
            if field == "eyr":
                valid &= int(val) >= 2020 and int(val) <= 2030
            if field == "hgt":
                if "cm" in val[-2:]:
                    h = int(val[0:-2])
                    valid &= h >= 150 and h <= 193
                elif "in" in val[-2:]:
                    h = int(val[0:-2])
                    valid &= h >= 59 and h <= 76
                else:
                    valid &= False
            if field == "hcl":
                valid &= (val[0] == '#') and len(val) == 7 and all((c>='0' and c<='9') or (c>='a' and c<='f') for c in val[1::])
            if field == "ecl":
                valid &= val in ["amb","blu","brn","gry","grn","hzl","oth"]
            if field == "pid":
                valid &= len(val) == 9 and all(c>='0' and c<='9' for c in val)
            print(valid)
            if not valid:
                break
        if valid:
            counter += 1
 
    print(counter)


main()
