# from sys import stdio
def main():
    # read da file
    file1 = open('./tht1.in', 'r') 
    Lines = file1.readlines() 

    # sort da mofo
    # get da numbas
    numbers = sorted([int(num) for num in Lines])
    #print(sorted(numbers)[::-1])
    for i in numbers:
        for j in numbers[::-1]:
            if i+j <= 2020:
                break
        if i+j == 2020:
            break
    print(i*j)
main()