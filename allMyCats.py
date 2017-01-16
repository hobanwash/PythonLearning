#chapter 4 list fun
catNames = []
while True:
    print('Enter the name of the cat ' + str(len(catNames) + 1) + ' (or put nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('The cat names are:')
for name in catNames:
    print(' ' + name)
    
