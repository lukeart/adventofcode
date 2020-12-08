def main(filein):
    print(sum([len(set(line.replace("\n",""))) for line in open(filein, 'r').read().split("\n\n")]))

main('6.lk.in')