import json
import os
import random

os.chdir(os.path.dirname(__file__))

amount = int(input('How many Usernames to generate:\n'))

minimum = int(input('Minimum amount of characters: (> 3)\n'))
maximum = int(input('Maximum amount of characters: (< 20)\n'))

characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


uList = {'Test'}

for i in range(amount):
    print(i)
    randomNum = random.randint(minimum, maximum)
    username = []
    for letter in range(randomNum):
        username.append(random.choice(characters))
    username = ''.join(username)
    uList.add(username)

uList = {i: item for i, item in enumerate(uList)}


with open('Ulist.json', 'r') as file:
    data = json.load(file)
    data['Usernames'] = uList

with open('Ulist.json', 'w') as file:
    json.dump(data, file, indent=4)