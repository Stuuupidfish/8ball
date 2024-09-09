import random

answers = [
    #affirmative answers
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    
    #non committal answers
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    
    #negative answers
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
    ]

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

