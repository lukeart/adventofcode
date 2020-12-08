

def main():
    file1 = open('./2.th.in', 'r')
    lines = file1.readlines()

    lines2 = [line.split() for line in lines]
    counter = 0
    for line in lines2:
        r1, r2 = line[0].split("-")
        c = line[1][0]
        p = line[2]
        print(r1, r2,c, p)
        count = p.count(c)
        if count >= int(r1) and count <= int(r2):
            counter+=1
    print(counter)



main()
