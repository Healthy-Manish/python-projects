# a dictionary that stores questions and answers
# have a variable that tricks the score of the player
# loop through the dictionary using the key values pairs 
# display each question to the  user and allow them to answer
# tell them if they are right or wrong 
# show the final result when quiz is completed
quiz = {
    "Question1": {"question": "what is the capital of france","answer":"paris"},
    "Question2":{"question":"What is the capital of Germany","answer":"Berlin"},
    "Question3":{"question":"what is the capital of Italy","answer":"Rome"},
    "Question4":{"question":"what is the capital of spain","answer":"madrid"},
    "Question5":{"question":"what is the capital of India","answer":"New Delhi"},
    "Question6":{"question":"what is the capital of Russia","answer":"Moscow"},
        }
score = 0
for key,value in quiz.items():
    print(value['question'])
    answer = input("Answer: ")
    if answer.lower()== value['answer'].lower():
        score+=1
        print("Correct answer :)")
    else:
        print("Wrong answer :(")

print(f"Your score is {score} out of ",len(quiz))