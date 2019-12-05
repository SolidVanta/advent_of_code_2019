with open("input", "r+") as file:
    summ = 0
    for line in file:
        summ = summ + int(line)/3-2
    print("Total = {}".format(summ))
