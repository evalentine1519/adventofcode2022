with open('day1data.txt', 'r') as f:
    data = f.read()
    f.close()

biggest = 0
bigger = 0
big = 0
total = 0
data = data.split('\n\n')
count = 0
values = []

for item in data:
    pieces = item.split('\n')
    #print(pieces)
    for piece in pieces:
        if piece != '':
            total += int(piece)
    values.append(total)
    total = 0
    
values.sort()
total = 0
total = total + values.pop()
total = total + values.pop()
total = total + values.pop()
print(total)