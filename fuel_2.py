
def calculate_fuel(result, the_sum, seq):
    result = (result//3 - 2)
    if result > 0:
        #the_sum = the_sum+result
        seq.append( result)
        return calculate_fuel(result, the_sum, seq)
    if result <= 0:
        return sum(seq)


print(calculate_fuel(100756,0,seq=[]))
#calculate_fuel(3421505,0,seq=[])

cum_sum=0
with open("input", "r+") as file:
    for line in file:
        cum_sum = cum_sum + calculate_fuel(int(line), 0, seq=[])
        print cum_sum

