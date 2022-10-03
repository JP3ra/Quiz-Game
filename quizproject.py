print("Do you want to play a game")
ans = str(input())

if ans.lower()=="yes":
    #initialising two variables to evaluate the final score
    score = 0
    total_score = 4

    print("Alright let's play the game!")
    print("\n")

    #question_1
    print("What is the full form of CPU")
    ans1 = str(input("Enter you answer: "))
    if ans1.lower() == "central processing unit":
        print("Correct answer!")
        score+=1
    else:
        print("You answer is incorrect!")
    print("\n")

    #question_2
    print("What is the full form of CD")
    ans2 = str(input("Enter the answer: "))
    if ans2.lower()=="compact disc":
        print("Correct Answer")
        score+=1
    else:
        print("Your answer is incorrect")
    
    print("\n")


    #question_3
    print("What is the full form of DVD")
    ans3 = str(input("Enter your answer: "))
    if ans3.lower()=="digital versatile disc":
        print("Correct Answer!")
        score+=1
    else:
        print("Incorrect answer")
    print("\n")
    
    #question_4
    print("What is the full form of SSD?")
    ans4 = str(input("Enter your answer: "))
    if ans4.lower() == "solid state drive":
        print("Correct Answer")
        score+=1
    else:
        print("Incorrect Answer")
    
    print("\n")
    
    #evaluating the final result 
    perc = (score/total_score*100)
    print("Your total score is: ", perc)
    print("Thanks for participating ")

else:
    #printing a friendly message to finish off the gap
    print("Alright! Will play some other time!")