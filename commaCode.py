def commaCode(list):
    if(len(list) < 2):
        return ''.join(list)

    x =', '.join(list).split()
    x.insert(-1, 'and')
    return ' '.join(x)
print(commaCode(['apples', 'bananas', 'tofu', 'cats']))
print(commaCode([]))
print(commaCode(['cart']))
