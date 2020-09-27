#! python3
# bulletPointsAdder.p - Adds wiki markup style bullet points at the start of each line to the text stored in clipboard

import pyperclip

text = pyperclip.paste()

lines =text.split('\n')
modifiedText = ''
for i in range(len(lines)):
    modifiedText += f'* {lines[i]}'
    if (i != len(lines) - 1 ):
        modifiedText += '\n'

pyperclip.copy(modifiedText)
