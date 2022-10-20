def menu(voc):
    #print('-' * 17)
    for k, v in voc.items():
        print(f'{k}: {v.__doc__}.', end = ' ')
    #print('\n' + '-' * 17)

def explore():
    '''Explore'''
    print('locations anywhere')

def stats():
    '''Stats'''
    print('stats here')

def equip():
    '''Equipment'''
    print('items there')

def skills():
    '''Skills'''
    print('skills.. where?..')

actions = {1: explore, 2: stats, 3: equip, 4: skills}


retry = 1
while retry != '00':
    menu(actions)
    retry = input('00: Save & Exit.\nChoose action: ')
    try:
        actions[int(retry)]()
    except:
        print('Choose proper action:')

print('Bye-bye, adventurer..')


