#! python3

# multiplicationQuiz.py - a timed multiplication quiz

import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correct = 0

for questionNum in range(numberOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = f'#{questionNum} {num1} X {num2} = ??\n'

    try:
        pyip.inputStr(prompt, 
                allowRegexes=[f'^{num1*num2}$'], 
                blockRegexes=[('.*', 'Incorrect')], 
                timeout=8,
                limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
        print(f'correct answer was {num1*num2}')
    except pyip.RetryLimitException:
        print('Out of tries!')
        print(f'correct answer was {num1*num2}')
    else:
        print('Correct!')
        correct += 1
    time.sleep(.5)

print(f'Final Score: {correct}/{numberOfQuestions}')
