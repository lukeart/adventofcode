def main(filein):
    file1 = open(filein, 'r')
    lines = file1.read().replace("F","0").replace('B','1').replace('L','0').replace('R','1').split('\n')
    seats=[int(e,2) for e in lines]
    seats.sort()

    prev, curr = 0,0
    for s in seats:
        prev = curr
        curr = s
        if s > seats[0] and s < (1024-8):
            if curr - prev > 1:
                break
    print(curr-1)

main('5.lk.in')