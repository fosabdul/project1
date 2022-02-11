""" This program is a trivia quiz program. The user selects a topic, and then is challenged to answer quiz questions 
on that topic. If the user gets a question correct, they see a 'Correct!' message. If their answer is incorrect, they see a message 
with the correct answer. After the user has answered all the questions, they will see the number of questions they answered correctly.  
 """


#This is the dictionary of topics with questions as it values
# indentation makes dictionaries more readable
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

# this function is called to get the topic of quiz from the user
# The user is able to choose the topics given
# it returns the name of the topic if it exists
# otherwise it returns False
def pick_quiz():   # use python naming conventions 
    while True:
        print('Please Choose the topics from the following :  ')
        for topic in questions:  # use descriptive variable names 
            print(topic)
        print('-----------------------------------------------')
        topic_choice = input('Would you like art, or space questions? ')  # this message wouldn't make sense if the topics change 
        if topic_choice in questions:
            return topic_choice
        # else:
        #     return False    # Can you ask the user to try again? A while loop would help

# Put an empty line or two between functions
        
def main():
    #It is the variable to hold the number of correct answers given by the user
    total_score = 0
    topic = pick_quiz()  # configure this function to return a topic 
    # if the user chooses the topic that does exist
    # the questions are displayed from the chosen topic

    topic_questions = questions[topic]   # can you think of a better variable name? 
    # This for loop displays the questions from the chosen topic
    for question in topic_questions:  # variable names 
        user_answer = input(question + " ")  # this is confusing to read - better variable names would hlep 
        # if the answer is correct then total_score increases by 1
        correct_answer = topic_questions[question]
        if user_answer.lower() == correct_answer.lower(): # be consistent with spacing around operators 
            total_score = total_score+1
            print('Your answer is correct ')
        else:# otherwise it prints the correct answer
            print('The correct answer was ', correct_answer)
    # At the end it prints the total Score out of 3  # what if there are more questions? 
    print(f'Your total score is {total_score} out of {len(topic_questions)} ')  # the length of the dictionary is the number of questions 
    # else:
    #     print('You chose incorrect topic')   # not needed 
        # if the user chose another than the topic in the dictionary.
main()