def collatz(number):
    if(number %2 == 0):
        return number //2 
    else:
        return 3* number +1

while (True):
    print('Enter a number:', end=' ')
    try:
        number = int(input())
    except ValueError:
        print('That\'s not a number.')
        continue
    break

while (number != 1):
    print(number)
    number = collatz(number)

print(number)


