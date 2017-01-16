#Chapter 3 magic 8 ball
import random
messages = ['It is certain',
    'It is decidedly so',
    'Yes',
    'Reply is hazy, try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is No',
    'Outlook is not so good',
    'Very doubtful']
pickMe = random.randint(0, len(messages) - 1)
print(messages[pickMe] + ' ' + str(pickMe))

