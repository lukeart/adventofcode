def aoc9a(filein, length):
    # convert entire input to list of integers
    lines = [int(l) for l in open(filein, 'r').read().split("\n")]
    buffer=[[]]

    # i is the current value that the buffer will be updated against
    for i in range(1,len(lines)-1):
        # how many values should we look back; it's less than length, if we've just started
        lookback = min(length-1, i)
        # if buffer isn't big enough, we need to expand it
        if len(buffer)<lookback:
            buffer.append([])
        # look over the previous `loopback` values and update the 2D buffer
        for j in range(0,lookback):
            buffer[j].append(lines[i-lookback+j]+lines[i])
        
        # if we're not ramping up anymore
        if len(buffer)==length-1:
            # create a set of all values
            s = set([x for lst in buffer for x in lst])
            # and check with the next (!) value is in
            if lines[i+1] not in s:
                print(lines[i+1])
            # get rid of the list of sums we don't need anymore
            buffer.pop(0)       

aoc9a("9.test.in", 5)
aoc9a("9.lk.in",25)