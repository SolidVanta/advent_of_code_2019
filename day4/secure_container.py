input_=(134792, 675810)
passwords=list()

def criterias_met(result):
    result = str(result)
    duplicate = False
    pos = 0
    while pos <= len(result):
        digit = result[pos]
        pos+=1
        try:
            if digit == result[pos] and not duplicate:
                duplicate = True
                continue
            elif digit == result[pos] and duplicate:
                result = result[0:pos-1]+ result[pos:]
                pos = pos-1
            elif digit != result[pos] and digit != result[pos+1]:
                duplicate=False
        except IndexError:
            break
    return int(result)

def is_incremental(test):
    test = str(test)
    for pos, digit in enumerate(test):
        try:
            if int(digit) > int(test[pos+1]):
                return False
            else:
                continue
        except IndexError:
            break
    return True

def contains_duplicate(sequence):
    sequence = str(sequence)
    duplicate = False
    for pos, digit in enumerate(sequence):
        pos += 1
        try:
            if (digit == sequence[pos]):
                duplicate = True
        except IndexError:
            break
    return duplicate

def match(number):
    number = criterias_met(number)
    if number != None:
        if contains_duplicate(number):
            if is_incremental(number):
                return True
    else:
        return False

'''
test  = 122222233333344445678888888
test  = 12345
test = 2221
test = 1234515
print(criterias_met(test))
print("Is it incremental? {}".format(is_incremental(test)))
print("Does it contain duplicates? {}".format(contains_duplicate(test)))
#print(contains_duplicate(test))
#print(match(test))
'''

start = input_[0]
end = input_[1]
while start != end:
    number = match(start)
    if number:
        passwords.append(number)
    start +=1
print(len(passwords))


