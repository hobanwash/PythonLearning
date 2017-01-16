#chapter 4 more list fun
myPets = ['Teddy', 'Josie', 'Tavie', 'Failte']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
