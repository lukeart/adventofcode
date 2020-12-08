def main():
    # width 31
    x = 0
    counter=0
    file1 = open('./3.th.in', 'r')
    lines = file1.readlines()
    for line in lines:
        if line[x] == '#':
            counter += 1
        x = (x + 3) % 31
    print(counter)

main()