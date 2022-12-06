def stack_build(stacklist):
    stacks = [[], [], [], [], [], [], [], [], []]
    for item in stacklist:
        temp = list(item[0])
        temp = temp[1::4]
        for index, item in enumerate(temp):
            if item != ' ':
                stacks[index].append(item)
    for stack in stacks:
        stack.reverse()
    return stacks

def move_build(movelist):
    for item in movelist:
        item[0] = item[0].split(' ')[1::2]
    return movelist

def mover(stacklist, moves):
    for move in moves:
        source = int(move[0][1]) - 1
        target = int(move[0][2]) - 1

        for i in range(int(move[0][0])):
            stacklist[target].append(stacklist[source].pop())
    
    answer = []
    for stack in stacklist:
        answer.append(stack.pop())
    return answer
        
def upgraded_mover(stacklist, moves):
    for move in moves:
        source = int(move[0][1]) - 1
        target = int(move[0][2]) - 1
        temp = []

        for i in range(int(move[0][0])):
            temp.append(stacklist[source].pop())
        for i in range(int(move[0][0])):
            stacklist[target].append(temp.pop())
    
    answer = []
    for stack in stacklist:
        answer.append(stack.pop())
    return answer

with open('day5data.txt', 'r') as f:
    data = [item.split('\n') for item in f]

for item in data:
    item.pop()

stacklist = []
movelist = []

for item in data:
    if data.index(item) < 8:
        stacklist.append(item)
    elif data.index(item) > 9:
        movelist.append(item)

stacks = stack_build(stacklist)
moves = move_build(movelist)
print(upgraded_mover(stacks, moves))