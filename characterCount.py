#characterCount

import pprint

print('Type or paste any message and this program will count the \
number of times each character shows up in your text.')

message = input('Enter some text: ')
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count, width=20)
