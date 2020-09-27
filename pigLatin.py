#! python3
# pigLatin.py - Promotes a user for a phrase and then prints out that phrase converted to piglatin

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y') 

print("Enter the phrase you would like converted to Pig Latin: ")
message = input()

pigLatin = []
for word in message.split():
    # Seperate non-letters at the start of the word:
    prefixNonLetters = ''
    while (len(word) > 0 and not word.isalpha()):
        prefixNonLetters += word[0]
        word = word[1:]

    # if the word isn't a word just add it back
    if(len(word) == 0):
        pigLatin.append(prefixNonLetters)
        continue

    # Seperate nonletters at the end of the word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]


    # remember casing
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()

    # remove consonate group at the start of the word
    prefixConsonant = ''
    while(len(word) > 0 and word[0] not in VOWELS):
        prefixConsonant += word[0]
        word = word[1:]

    ## add consonate and piglatin ending to word
    if prefixConsonant:
        word += prefixConsonant + 'ay'
    else:
        word += 'yay'

    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non leters back
    word = prefixNonLetters + word + suffixNonLetters

    # Add word to phrase
    pigLatin.append(word)

print(' '.join(pigLatin))
