class Rucksack:
    def __init__(self, data):
        self.first = data[:len(data)//2]
        self.second = data[len(data)//2:len(data)]

    def find_same(self):
        self.firstset = set(self.first)
        self.secondset = set(self.second)
        self.same = self.firstset.intersection(self.secondset).pop()

    def get_priority(self):
        self.find_same()
        if ord(self.same) > 96:
            return ord(self.same) - 96
        else:
            return ord(self.same) - 38

class Group:
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third

    def find_same(self):
        self.firstset = set(self.first)
        self.secondset = set(self.second)
        self.thirdset = set(self.third)
        self.same = self.firstset.intersection(self.secondset, self.thirdset).pop()

    def get_priority(self):
        self.find_same()
        if ord(self.same) > 96:
            return ord(self.same) - 96
        else:
            return ord(self.same) - 38




with open('day3data.txt', 'r') as f:
   data = [line.rstrip('\n') for line in f] 

items = [Rucksack(item) for item in data]
total = 0
for item in items:
    total += item.get_priority()
print(total)

groups = []
for item in data:
    if data.index(item) % 3 == 0:
        first = item
    elif data.index(item) % 3 == 1:
        second = item
    else:
        third = item
        groups.append(Group(first, second, third))

group_total = 0
for item in groups:
    group_total += item.get_priority()

print(group_total)
