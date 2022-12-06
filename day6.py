with open('day6data.txt', 'r') as f:
    data = f.read()

def detector(buffer, marker_length):
    temp = []
    tempset = set()
    for i, char in enumerate(buffer):
        if i < marker_length:
            temp.append(char)
        else:
            tempset = set(temp)
            if len(tempset) == marker_length:
                return i
            else:
                tempset = set()
                temp.pop(0)
                temp.append(char)

print(detector(data, 4))
print(detector(data, 14))