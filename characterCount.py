#more fun from Chap 5
import pprint
message = 'It was a cold and rainy Saturday and I was planning on spending the time mastering Python'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
