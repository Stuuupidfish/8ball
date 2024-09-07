import random

answers = []

#affirmative answers
answers.append("It is certain")
answers.append("It is decidedly so")
answers.append("Without a doubt")
answers.append("Yes definitely")
answers.append("You may rely on it")
answers.append("As I see it, yes")
answers.append("Most likely")
answers.append("Outlook good")
answers.append("Yes")
answers.append("Signs point to yes")

#non committal answers
answers.append("Reply hazy, try again")
answers.append("Ask again later")
answers.append("Better not tell you now")
answers.append("Cannot predict now")
answers.append("Concentrate and ask again")

#negative answers
answers.append("Don't count on it")
answers.append("My reply is no")
answers.append("My sources say no")
answers.append("Outlook not so good")
answers.append("Very doubtful")

#checking and making sure everything is where its supposed to be:
    # print(answers)
    # print(len(answers))
    # print(answers[19])

runProgram = True

def endOrLoopProgram():
    global runProgram
    question = input("Do you want to ask again? type yes or no \n")
    if question.lower() == "yes":
        return
    if question.lower() == "no":
        runProgram = False
    else:
        print("Sorry I didn't catch that.")
        return endOrLoopProgram()

while runProgram:
    pickRandomAnswer = random.randint(0, len(answers)-1)
    input("Ask me a question and I will give you an answer \n")
    print(answers[pickRandomAnswer])
    endOrLoopProgram()


