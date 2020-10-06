#! python3

# sandwhichShop.py - a input based sandwhich shop

import pyinputplus as pyip

menu = {
        'wheat': 1.00,
        'white': .50,
        'sourdough': 1.30,
        'chicken': 1.00,
        'turkey': 1.40,
        'ham': .70,
        'tofu': 2.00,
        'chedder':.45,
        'swiss': .35,
        'mozzarella': 55,
        'mayo': .05,
        'mustard': .05,
        'lettuce': .15,
        'tomato': .25
}

total = 0
total += menu[pyip.inputMenu(['wheat', 'white', 'sourdough'], 
    prompt='What type of bread do you want? \n',
    numbered=True)]

total += menu[pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], 
    prompt='What type of protein do you want? \n',
    numbered=True)]

if(pyip.inputYesNo('Do you want cheese?') == 'yes'):
    total += menu[pyip.inputMenu(['chedder', 'swiss', 'mozzarella'], 
        prompt='What type of cheese do you want? \n',
        numbered=True)]


if(pyip.inputYesNo('Do you want mayo?\n') == 'yes'):
    total += menu['mayo']

if(pyip.inputYesNo('Do you want mustard?\n') == 'yes'):
    total += menu['mustard']


if(pyip.inputYesNo('Do you want lettuce?\n') == 'yes'):
    total += menu['lettuce']

if(pyip.inputYesNo('Do you want tomato?\n') == 'yes'):
    total += menu['tomato']

numSandwhiches = pyip.inputInt('How many sandwhiches do you want?', min=0 )

print(f'Your sandwhich costs ${total*numSandwhiches}')
