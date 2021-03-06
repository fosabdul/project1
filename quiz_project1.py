""" This program is a trivia quiz program. """""

# I have commented all my code the older MyoldQuiz.py 

questions = {
    'art': {
        'Who painted the Mona Lisa?': 'Leonardo Da Vinci',
        'What precious stone is used to make the artist\'s pigment ultramarine?':'Lapiz lazuli',
        'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?':'Chicago'
    },
    'space': {
        'Which planet is closest to the sun?':'Mercury',
        'Which planet spins in the opposite direction to all the others in the solar system?':'Venus',
        'How many moons does Mars have?':'2'
    }
}


def main():
   
    total_score = 0

    topic = input('Would you like art, or space questions? ')
    
    topic_questions = questions[topic]   
    
    for question in topic_questions:  
        user_answer = input(question + " ")  
        correct_answer = topic_questions[question]

        if user_answer.lower() == correct_answer.lower(): 
            total_score = total_score+1
            print('Your answer is correct ')
        else:
            print('The correct answer was ', correct_answer)

    
    print(f'Your total score is {total_score} out of {len(topic_questions)} ')  
print('You chose incorrect topic')


main()