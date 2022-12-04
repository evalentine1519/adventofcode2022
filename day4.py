class Group:
    def __init__(self, input):
        self.first = input[0].split('-')
        self.second = input[1].split('-')

    def set_gen(self):
        self.firstset = set(range(int(self.first[0]), int(self.first[1]) + 1))
        self.secondset = set(range(int(self.second[0]), int(self.second[1]) + 1))

    def contains(self):
        if self.firstset.issubset(self.secondset) or self.secondset.issubset(self.firstset):
            return True
        else:
            return False
    
    def overlap(self):
        if self.firstset.isdisjoint(self.secondset) is False:
            return True
        else:
            return False

with open('day4data.txt', 'r') as f:
    data = [item.rstrip('\n') for item in f]

groups = [Group(item.split(',')) for item in data]

total = 0
total_overlap = 0
for group in groups:
    group.set_gen()
    if group.contains() is True:
        total += 1
    if group.overlap() is True:
        total_overlap += 1
print(total)
print(total_overlap)