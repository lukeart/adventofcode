
# from sys import stdio
def main():
    file1 = open('./1.in', 'r')
    Lines = file1.readlines()

    numbers = sorted([int(num) for num in Lines])
    win=False
    # print(sorted(numbers)[::-1])
    for i in numbers:
        for j in numbers[::-1]:
            if (2020-i-j) in numbers:            
                win=True
                break
        if win:
            break
    print(i,j,i*j*(2020-i-j))


main()
