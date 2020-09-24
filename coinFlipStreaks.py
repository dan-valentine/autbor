import random

def flipCoin():
    if(random.randint(0, 1) == 0):
        return 'H' 
    return 'T'

streaks = 0
for _i in range(10000):
    set = ''

    for _j in range(100):
        set += flipCoin()

    if('TTTTTT' in set or 'HHHHHH' in set):
        streaks += 1
    print(set)

print('Chance of streaks %s%%' % (streaks / 100))
