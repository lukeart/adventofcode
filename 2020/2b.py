

def main():
    file1 = open('./2.lk.in', 'r')
    lines = file1.readlines()

    lines2 = [line.split() for line in lines]
    counter = 0
    for line in lines2:
        r1, r2 = line[0].split("-")
        c = line[1][0]
        p = line[2]
        print(r1, r2,c, p)
        if (p[int(r1)-1] == c) ^ (p[int(r2)-1] == c):
            counter+=1
    print(counter)



main()
