#! python3

# randomQuizGenerator.py - generates quizes and anwsers in a random order along with answer keys 

import random
import pyinputplus as pyip

CAPITALS = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'  
}

ABCD = 'ABCD'

numQuizes = pyip.inputNum('How many quizes would you like to generate?\n', min=1)
numQuestions = pyip.inputNum('How many questions should each quiz be?\n', min=1, max=50)

for quizNum in range(numQuizes):
    # create files
    quizFile = open(f'capitalsQuiz{quizNum+1}.txt', 'w')
    answersFile = open(f'capitalsQuiz{quizNum+1}.answers.txt', 'w')

    # create quiz header
    quizFile.write('Name:\nDate:\n\n\n\nCapitals Quiz\n\n\n')

    # shuffle the states
    states = list(CAPITALS.keys())
    random.shuffle(states)

    # create a list of as many questions as wanted
    states = states[:numQuestions]

    # get options for answers
    for questionNum in range(numQuestions):
        correctAnswer = CAPITALS[states[questionNum]]
        wrongAnswers = list(CAPITALS.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        options = wrongAnswers + [correctAnswer]
        random.shuffle(options)
        
        # write answer to answer key
        answersFile.write(f'{questionNum+1}. {ABCD[options.index(correctAnswer)]}\n')

        # write question to question file
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')

        for i in range(4):
            quizFile.write(f'\t{ABCD[i]}. {options[i]}\n')
    
    quizFile.close()
    answersFile.close()
