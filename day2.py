with open('day2data.txt', 'r') as f:
    moves = f.read()
    f.close()

moves = moves.split('\n')
moves.pop()

def part_one(data):
    total = 0
    for item in data:
        piece = item.split(' ')
        match piece[1]:
            case 'X':
                total += 1
                if piece[0] == 'C':
                    total += 6
                elif piece[0] == 'A':
                    total += 3
                else:
                    pass
            case 'Y':
                total += 2
                if piece[0] == 'A':
                    total += 6
                elif piece[0] == 'B':
                    total += 3
                else:
                    pass
            case 'Z':
                total += 3
                if piece[0] == 'B':
                    total += 6
                elif piece[0] == 'C':
                    total += 3
                else:
                    pass
    return total

def part_two(data):
    total = 0
    for item in data:
        piece = item.split(' ')
        match piece[1]:
            case 'X':
                total += 0
                if piece[0] == 'C':
                    total += 2
                elif piece[0] == 'A':
                    total += 3
                else:
                    total += 1
            case 'Y':
                total += 3
                if piece[0] == 'A':
                    total += 1
                elif piece[0] == 'B':
                    total += 2
                else:
                    total += 3
            case 'Z':
                total += 6
                if piece[0] == 'B':
                    total += 3
                elif piece[0] == 'C':
                    total += 1
                else:
                    total += 2
    return total

print(part_one(moves))
print(part_two(moves))