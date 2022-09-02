#a dictionary that stores questions and answers
# have a variable that tracks the score of the player
# Loop through the dic using the key value pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is completed


quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Italy",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of USA",
        "answer": "Washington DC"
    },
    "question5": {
        "question": "What is the capital of Portugal",
        "answer": "Lisbon"
    },
    "question6": {
        "question": "What is the capital of Switzerland",
        "answer": "Bern"
    },
    "question7": {
        "question": "What is the capital of Austria",
        "answer": "Vienna"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer?:  ")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print(f"Your score is {score}")

    else:
        print("Wrong!")
        print("The answer is: " + value['answer'])
        print(f"Your score is {score}")
    
