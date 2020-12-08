def main(filein):
    file1 = open(filein, 'r')
    lines = file1.read().replace("F","0").replace('B','1').replace('L','0').replace('R','1').split('\n')
    print(max([int(e,2) for e in lines]))

main('5.lk.in')