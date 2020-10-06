#! python3

# keepAnIdiotBusy.py - a script to keep an idiot busy

import pyinputplus as pyip

while True:
    prompt = 'Do you want to know how to keep an idot busy for hours?\n'
    response = pyip.inputYesNo(prompt)
    if(response == 'no'):
        break

print('Thank you have a nice day! :)')
