""" A quiz program. """

total_score = 0

topic = input('Would you like art, or space questions? ')

if topic == 'art':

    # if topic == 'art' | topic == 'space':

    Q1Art = input('Who painted the Mona Lisa?')
    Q2Art = input('What precious stone is used to make the artist\'s pigment ultramarine?')
    Q3Art = input('Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?')
    


    if Q1Art == 'Leonardo Da Vinci':
        print('Correct!')
        total_score += 1
    else:
        print('Sorry, the answer is Leonardo Da Vinci.')
    
    Q2Art = input('What precious stone is used to make the artist\'s pigment ultramarine?')
    if Q2Art == 'Lapiz lazuli':
        print('Correct!')
        total_score += 1
    else:
        print('Sorry, the correct answer is Lapiz lazuli.')

    Q3Art = input('Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?')
    
    if Q3Art == 'Chicago':

        print('Correct!')
        total_score += 1
    else:
        print('Sorry, the correct answer is Chicago.')

    print('End of quiz!')

    print(f'Your total score on {topic} questions is {total_score} out of 3.')

    if total_score == 3:
        print('You got all the answers correct!')


elif topic == 'space':
    
    print('Which planet is closest to the sun?')
    answer = input('Enter your answer: ')
    if answer == 'Mercury':
        print('Correct!')
        total_score += 1
    else:
        print('Sorry, the correct answer is Mercury.')

    print('Which planet spins in the opposite direction to all the others in the solar system?')
    answer = input('Enter your answer: ')
    if answer == 'Venus':
        print('Correct!')
        total_score += 1
    else:
        print('Sorry, the correct answer is Venus.')

    print('How many moons does Mars have?')
    answer = input('Enter your answer: ')
    if answer == '2':   
        print('Correct!')
        total_score += 1
    else:
        print('Sorry, the correct answer is 2.')

    print('End of quiz!')
    print(f'Your total score on {topic} questions is {total_score} out of 3.')

    if total_score == 3:
        print('You got all the answers correct!')

else:
    print('That is not a valid topic.')
