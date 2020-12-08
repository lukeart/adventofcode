def main(filein):
    lines = open(filein, 'r').read().split("\n\n")
    count=0
    for line in lines:
        pp = line.split("\n")
        num = len(pp)
        all_answers = "".join(pp)
        all_answers_set = set(all_answers)
        for a in all_answers_set:
            count +=1 if all_answers.count(a) == num else 0
        print(len(list(filter(lambda x: all_answers.count(x) == num, all_answers_set))))
    print(count)
        

main('6.lk.in')