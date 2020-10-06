#! python3
# clipBoardToPhoneEmails - Finds all the phone numbers and emails in the clipboard and writes them to the clipboard

import pyperclip, re

# phone number regex
phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?              # area code
        (\s|-|\.)?                      # seperator
        (\d{3})                         # first 3 letters
        (\s|-|\.)?                      # seperator
        (\d{4})                         # last 4 letters
        (\s*(ext|ext.|x)\s*(\d{2,5}))?   # ext
        )''', re.VERBOSE)

# email regex
emailRegex = re.compile(r'''(
        [a-zA-Z0-9.%_+-]+   # username
        @                   # at symbol
        [a-zA-Z0-9.-]+      # domain
        (\.[a-zA-Z]{2,4})   # dot somethin
        )''', re.VERBOSE)

# find matches in clipboard
text = str(pyperclip.paste())

matches = []
for phoneGroup in phoneRegex.findall(text):
    phoneNumber = '-'.join([phoneGroup[1], phoneGroup[3], phoneGroup[5]])
    if phoneGroup[8]:
        phoneNumber += f' x{phone[8]}'
    matches.append(phoneNumber)

for emailGroup in emailRegex.findall(text):
    matches.append(emailGroup[0])

#write matches to clip board
if len(matches):
    pyperclip.copy('\n'.join(matches))
    print('matches found: \n')
    print('\n'.join(matches))
else:
    print('no matches found')
