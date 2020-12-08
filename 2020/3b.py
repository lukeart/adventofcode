def main():
    # width 31
    x1, x2, x3, x4, x5 = 0,0,0,0,0
    c1, c2, c3, c4, c5 = 0,0,0,0,0
    file1 = open('./3.th.in', 'r')
    lines = file1.readlines()
    odd = True
    for line in lines:
        if line[x1] == '#':
            c1 += 1
        x1 = (x1 + 1) % 31
        if line[x2] == '#':
            c2 += 1
        x2 = (x2 + 3) % 31
        if line[x3] == '#':
            c3 += 1
        x3 = (x3 + 5) % 31
        if line[x4] == '#':
            c4 += 1
        x4 = (x4 + 7) % 31
        if odd:
            if line[x5] == '#':
                c5 += 1
            x5 = (x5 + 1) % 31

        odd = not odd
    print(c1 , c2 , c3 ,c4,c5, c1 * c2 * c3 * c4 * c5)

main()