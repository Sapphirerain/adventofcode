"""part 1"""
# set up input file
input_path = './input3.txt'
with open(input_path) as f:
    paths = f.readlines()
    f.close()

paths = [line.strip('\n').split(',') for line in paths]

class Wire:
    def __init__(self):
        self.currX, self.currY = 0, 0
        self.coords = []

    def move(self, path):
        #print(path)
        dir = path[0]
        units = int(path[1:])

        if dir == 'U':
            self.coords = [(self.currX, self.currY + y) for y in range(1, units + 1)]
            self.currY += units
        elif dir == 'D':
            self.coords = [(self.currX, self.currY - y) for y in range(1, units + 1)]
            self.currY -= units
        elif dir == 'R':
            self.coords = [(self.currX + x, self.currY) for x in range(1, units + 1)]
            self.currX += units
        else:
            self.coords = [(self.currX - x, self.currY) for x in range(1, units + 1)]
            self.currX -= units
        return self.coords

temp = ['U10','R5', 'U3', 'L10']
temp2 = ['D5','R2','U20']
wire1 = Wire()
wire2 = Wire()
#wire1.coords += [wire1.move(path) for path in temp if type(path) == str]
#wire2.coords += [wire2.move(path) for path in temp2 if type(path) == str]

wire1.coords += [wire1.move(path) for path in paths[0] if type(path) == str]
wire2.coords += [wire2.move(path) for path in paths[1] if type(path) == str]

# flatten lists
wire1.coords = [item for sublist in wire1.coords for item in sublist]
wire2.coords = [item for sublist in wire2.coords for item in sublist]
# make sets
wire1_set = set(wire1.coords)
wire2_set = set(wire2.coords)
# find intersections
common  = set(wire1_set & wire2_set)
print(common)

def distance(coord):
    return abs(coord[0]) + abs(coord[1])

distances = [distance(coord) for coord in common]
#print(distances)
print(min(distances))

"""part 2"""
#print(wire1.coords)
#print(wire2.coords)
wire_dists = [wire1.coords.index(x) + wire2.coords.index(x) + 2 for x in common]
#print(wire_dists)
print(min(wire_dists))
