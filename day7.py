class File:
    def __init__(self, size, name, parents):
        self.size = size
        self.name = name
        self.parents = '/'.join(parents)
        self.id = name +str(size)

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return str(self.parents) + str(self.size)

def update_folders(files, folders):
    for file in files:
        parents = file.parents
        size = file.size
        while len(parents) > 0:
            combined_size = size + folders.get(parents)
            folders.update({parents: combined_size})
            parents = parents.split('/')
            parents.pop()
            parents = '/'.join(parents)


with open('day7data.txt', 'r') as f:
    data = [item.strip() for item in f]

working_dir = []
unique_dirs = {'/'}
files = set()

for item in data:
    text = item.split()

    if text[0] == "$":
        if text[1] == 'ls':
            continue
        elif text[1] == 'cd':
            if text[2] == '/':
                working_dir.clear()
                working_dir.append('/')
            elif text[2] == '..':
                working_dir.pop()
            else:
                working_dir.append(text[2])
                
    else:
        if text[0] == 'dir':
            unique_dirs.add('/'.join(working_dir) + '/' + text[1])
        else:
            files.add(File(int(text[0]), text[1], working_dir))

directories = dict.fromkeys(unique_dirs, 0)

update_folders(files, directories)

total = 0

#part 1 answer
for k, v in directories.items():
    if v < 100001:
        total += v

#part 2 answer
total_space = 70000000
needed_space = 30000000
used_space = directories.get('/')
free_space = total_space - used_space
needs_freeing = needed_space - free_space
options = []

for k, v in directories.items():
    if v > needs_freeing:
        options.append(v)
print(min(options))