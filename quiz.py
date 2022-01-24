""" A quiz program. """
# this will count the quiz with the 
total_score = 0
questions = 0

# the user can choose 
topic = input('Would you like art, or space questions? ')

#  if the user chose art they will be ask this three questions
if topic == 'art':

    while questions<=3: 
                    # question 1 

        ques1 =input("Who painted the Mona Lisa?  ")
        if ques1=="Leonardo Da Vinci":
            print('Correct!')
            total_score+=1
        else:
             print('Sorry, the answer is Leonardo Da Vinci.')

            # Question 2 

        ques2 =input("What precious stone is used to make the artist\'s pigment ultramarine?  ")
        if ques2=="Lapiz lazuli":
            print('Correct!')
            total_score+=1
        else:
            print('Sorry, the correct answer is Lapiz lazuli.')

            # Question 3
    
        ques3=input('Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?')
        if ques3 == 'Chicago':
            print('Correct!')
            total_score += 1

        else:
            print('Sorry, the correct answer is Chicago.')

        break

    print('End of quiz!')
    print(f'Your total score on {topic} questions is {total_score} out of 3.')

    if total_score == 3:
        print('You got all the answers correct!') 
        # """"if they answer all the questions""""


elif topic == 'space':
    
    spcQues1 = input('Which planet is closest to the sun?   ')
   
    if spcQues1 == 'Mercury':
        print('Correct!')
        total_score += 1
    else:
        print('Sorry, the correct answer is Mercury.   ')

    qspcQues2 = input('Which planet spins in the opposite direction to all the others in the solar system?')
    
    if spcQues1 == 'Venus':
        print('Correct!')
        total_score += 1
    else:
        print('Sorry, the correct answer is Venus.')

    spcQues3 = input('How many moons does Mars have?  ')
    
    if spcQues3 == '2':   
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

    # if the user type other than the topic   
