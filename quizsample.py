
from pydoc_data.topics import topics


score=0
i=1
topic = input("'Would you like art, or space questions? '")
if topic == "art":




    while i<=3: 

        ans=input("Who is the developer of Python")
        if ans=="Rouson":
            score+=1
        else:
            print("You are wrong !!!  Then the right is Rouson")


        ans=input("Who is this")
        if ans=="Fos":
            score+=1
        else:
            print("You are wrong !!!  Then the right is Fos")


        ans=input("Student")
        if ans=="abdul":
            score+=1
        else:
            print("You are wrong !!!  Then the right is abdul")
    
        break
else:
    topic == "space":
    
print('End of quiz!')

print('Your total score on questions is {score} out of 3.', score )



