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
    
    
    print('-----------------------------------------------')
    topic = input('Would you like art, or space questions? ')
    if topic in questions:   # if you have the chosen topic in the questions dictionary  
        return topic
    else:
        return False


def main():
    #It is the variable to hold the number of correct answers given by the user
    total_score = 0
    status=pickQuiz()
    
    # if the user chooses the topic that does exist
    # the questions are displayed from the chosen topic
    if status!=False:
        test=questions[status]
        # This for loop displays the questions from the chosen topic
        
        for i in test:
            x=input(i+" ")
            # if the answer is correct then total_score increases by 1
            if x.lower()==test[i].lower():
                total_score=total_score+1
                print('Your answer is correct ')
            else:# otherwise it prints the correct answer
                print('The correct answer was ',test[i])
        # At the end it prints the total Score out of 3
        print(f'Your total score is {total_score} out of 3 ')
    
    
    else:
        print('You chose incorrect topic')

        # if the user chose another than the topic in the dictionary.





main()