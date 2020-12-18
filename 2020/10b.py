def aoc10b(filein):
    # convert entire input to list of integers
    lines = [int(l) for l in open(filein, 'r').read().split("\n")]
    lines.sort()

    lines = [0]+lines+[max(lines)+3]
    conns = [1]+[0]*lines[-1]
    for i in lines[1:]:
        conns[i] = conns[i-1]+conns[i-2]+conns[i-3]
    print(conns[-1])


aoc10b("10.test.in")
aoc10b("10.lk.in")