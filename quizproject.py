""" This program is a trivia quiz program. The user selects a topic, and then is challenged to answer quiz questions 
on that topic. If the user gets a question correct, they see a 'Correct!' message. If their answer is incorrect, they see a message 
with the correct answer. After the user has answered all the questions, they will see the number of questions they answered correctly.  
 """


#This is the dictionary of topics with questions as it values
questions = { 'art':{'Who painted the Mona Lisa?':'Leonardo Da Vinci',
'What precious stone is used to make the artist\'s pigment ultramarine?':'Lapiz lazuli',
'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?':'Chicago'
                   },
'space':{'Which planet is closest to the sun?':'Mercury',
'Which planet spins in the opposite direction to all the others in the solar system?':'Venus',
'How many moons does Mars have?':'2'
}
}
# this function is called to get the topic of quiz from the user
# The user is able to choose the topics given
# it returns the name of the topic if it exists
# otherwise it returns False
def pickQuiz():

    print('Please Choose the topics from the following :  ')
    for list_of_topics in questions:
        print(list_of_topics)   # you will see all the topics in list 
    

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