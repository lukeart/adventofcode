def main(filein):
    lines = open(filein, 'r').read().split("\n\n")
    count=0
    for line in lines:
        pp = line.split("\n")
        num = len(pp)
        all_answers = "".join(pp)
        all_answers_set = set(all_answers)
        count += len(list(filter(lambda x: all_answers.count(x) == num, all_answers_set)))
    print(count)
        

main('6.lk.in')