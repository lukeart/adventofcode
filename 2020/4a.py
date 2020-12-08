#import re
def main():


    file1 = open('./4.lk.in', 'r')
    lines = file1.read()
    counter = 0
    passports = lines.split("\n\n")
    for p in passports:
        elements = p.replace('\n',' ').split()
        filtered_elements=list(filter(lambda e: "cid:" not in e, elements))
        #print(len(filtered_elements))
        if len(filtered_elements) == 7:
            counter += 1
        

    print(counter)

main()