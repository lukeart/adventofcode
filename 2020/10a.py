def aoc10a(filein):
    lines = [int(l) for l in open(filein, 'r').read().split("\n")]
    lines.sort()
    jolt1, jolt2, jolt3, old = 0,0,1,0
    for i in range(len(lines)):
        diff = lines[i]-old
        if diff == 1:
            jolt1 += 1
        elif diff == 2:
            jolt2 += 1
        elif diff == 3:
            jolt3 += 1
        old = lines[i]
    print(jolt1*jolt3)

aoc10a("10.test.in")
aoc10a("10.lk.in")