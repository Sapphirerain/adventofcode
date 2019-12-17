"""part 1/2"""
# set up input file
input_path = './input2.txt'
with open(input_path) as f:
    all = f.read().split(',')
    all = [int(x) for x in all]
    f.close()

# 1202 program alarm state
all[1] = 12
all[2] = 2
# part 2 inputs 
# output = all[0] = 19690720
all[1] = 98
all[2] = 20

curr = 0
# run intcode for every set of 4 nums until 99 or end of list is reached
while curr < len(all):
    # end program for opcode 99
    if all[curr] == 99:
        break
    op, in1, in2, out = [x for x in all[curr : curr+4]]
    # add values at in1 and in2 together
    if op == 1:
        all[out] = all[in1] + all[in2]
        print(in1,":",all[in1],"+",in2,":",all[in2],"=",out,":",all[out])
    # multiply values at in1 and in2 together
    elif op == 2:
        all[out] = all[in1] * all[in2]
        print(in1,":",all[in1],"*",in2,":",all[in2],"=",out,":",all[out])
    curr += 4

print(all[0])
