#! python3
# mclip.py - A multi-clipboard program 


import sys, pyperclip

TEXT = {
    'agree' : """Sounds Good""",
    'busy': """Can we do it sometime later this week or next week?""",
    'cancel': """Sorry, I am busy that day. Can you check back in next week?"""
}

if(len(sys.argv) < 2):
    print("Usage 'mclip.py <keyphase>' - copies Keyphrase to keyboard")
    sys.exit()

keyphrase = sys.argv[1]

if(keyphrase in TEXT):
    pyperclip.copy(TEXT[keyphrase])
    print(f'Text for keyphrase {keyphrase} copied to clipboard')
else:
    print(f'keyphrase {keyphrase} not found')


