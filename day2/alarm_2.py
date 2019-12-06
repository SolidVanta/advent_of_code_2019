
def traverse_and_calculate(noun, verb, seq):
    def one(pos):
        seq[seq[pos+3]] = seq[seq[pos+1]] + seq[seq[pos+2]]
        return seq

    def two(pos):
        seq[seq[pos+3]] = seq[seq[pos+1]] * seq[seq[pos+2]]
        return seq

    def ninenine():
        print seq

    idx = 0
    seq[1] = noun
    seq[2] = verb
    while seq[idx] != 99:
        if seq[idx] == 1:
            one(idx)
        elif seq[idx] == 2:
            two(idx)
        idx += 4
    return seq




seq = list()
with open("input_2","r+") as f:
    for line in f:
        for num in line.split(','):
            seq.append(int(num))




for i in range(100):
    for j in range(100):
        res = traverse_and_calculate(i, j, seq[:])
        if res[0] == 19690720:
            print(100 * i + j)
            print(res[0])
