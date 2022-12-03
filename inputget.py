import requests

day = int(input("What day do you want to get input for? "))
SESSION_ID = '53616c7465645f5f4cd0a8cbc20494a9485cdc42faf10fdbbfcf5197b4e1b3115fdbf997d17954bbc797f086252a22832ab06806e970b94866de6ce830a418ab'

input = requests.get(f'https://adventofcode.com/2022/day/{day}/input', cookies={"session": SESSION_ID}).text
with open(f'day{day}data.txt', 'w') as f:
    for line in input:
        f.write(line)
    f.close()