import math

"""part 1"""
# set up input file
input_path = './input.txt'
with open(input_path) as f:
    x = f.readlines()
f.close()

def calculate_fuel(mass):
    return math.floor(int(mass) // 3) - 2

# calculate fuel
fuels = [calculate_fuel(mass) for mass in x]
print(sum(fuels))

"""part 2"""
# calculate all fuel
def fuel_sum(fuel):
    req_fuel = calculate_fuel(fuel)
    if req_fuel <= 0:
        return 0
    return req_fuel + fuel_sum(req_fuel)

print(sum(fuel_sum(mass) for mass in x))
