"""part 1"""
# returns true if there are two same adjacent digits 
def same_adj(num_str):
    i = 0
    while (i < len(num_str) - 1):
        if num_str[i] == num_str[i + 1]:
            return True
        i += 1
    return False

# returns true if digits from left to right never decrease
def is_increasing(num_str):
    i = 0
    while (i < len(num_str) - 1):
        if int(num_str[i]) > int(num_str[i + 1]):
            return False
        i += 1
    return True

pass_range = range(240920, 789857 + 1)
count = 0
# count number of valid passwords
for i in pass_range:
    if is_increasing(str(i)) and same_adj(str(i)):
        count += 1
        #print(i)

print(count)

"""part 2"""
# returns true if there is at least one pair of adjacent identical digits
def has_double(num_str):
    i = 0
    chain = 1

    # iterate through string until an identical pair is found
    while (i < len(num_str) - 1):
        if chain == 2 and num_str[i] != num_str[i + 1]:
            return True
        if num_str[i] == num_str[i + 1]:
            chain += 1
        else:
            chain = 1
        i += 1

    # catch doubles at the end
    if chain == 2:
        return True
    return False

count = 0
# count number of valid passwords
for i in pass_range:
    if is_increasing(str(i)) and has_double(str(i)):
        count += 1

print(count)
