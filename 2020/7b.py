
def find_bag(rules, search_bag):
    ans = set()
    for (key, cont) in rules:
        for (cnt, bag) in cont:
            if bag == search_bag:
                ans.add(key)
                ans.update(find_bag(rules,key))
                break
    return ans

def find_bag_count(rules,search_bag):
    ans = 0
    for (key, cont) in rules:
        # should use Dict here
        if search_bag == key:
            for (cnt, bag) in cont:
                #print(search_bag,cnt,bag)
                ans += cnt * (1+find_bag_count(rules,bag))
    return ans

def main(filein):
    lines = open(filein, 'r').read().split("\n")
    rules = []
    for line in lines:
        words = line.split()
        container = words[0]+words[1]
        cont = []
        if words[4] != "no":
            pos = 4
            while pos < len(words):
                quant = int(words[pos])
                bag = words[pos+1]+words[pos+2]
                cont.append((quant,bag))
                pos += 4
        rules.append((container,cont))
    #print(rules)
    print(find_bag_count(rules,"shinygold"))

main("7.lk.in")