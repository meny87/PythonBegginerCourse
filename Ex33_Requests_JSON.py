import requests
import json
import pprint as ppt
import random

cnt = 1

print("***** Welcome to Computer Science Trivia **********")

while True:
    print("Question #", cnt)
    questionRaw = requests.get(
        "https://opentdb.com/api.php?amount=1&category=18&difficulty=hard&type=multiple")
    q = json.loads(questionRaw.text)
    print(q["results"][0]["question"])

    answers = q["results"][0]["incorrect_answers"]
    correct_answer = q["results"][0]["correct_answer"]
    answers.append(correct_answer)
    random.shuffle(answers)

    i = 1

    for ans in answers:
        print("\t" + str(i) + ".- " + ans)
        i += 1

    # Validate user option
    while True:
        try:
            opt = int(input("Choose an option: "))
            if opt <= 0 or opt > 4:
                print("Invalid option, please try again.")
            else:
                break
        except:
            print("Invalid answer. Use only numbers.")

    selected_answer = answers[opt - 1]
    if (selected_answer == correct_answer):
        print("Correct Answer!!!")
    else:
        print("Incorrect Answer, the correct answer was: ", correct_answer)

    # Validate user option
    while True:
        keepPlaying = input("Do you want to play again? [y/n]: ").lower()
        if keepPlaying == "n" or keepPlaying == "y":
            break
        else:
            print("Invalid option, please use 'y/Y' or 'n/N'.")

    if keepPlaying.lower() == "n":
        break
    else:
        cnt += 1
