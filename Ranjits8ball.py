import random

answers = [
  "It is certain",
  "It is decidedly so", "Without ad oubt", "Yes definitely", "You may rely on it","As I can see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"
]
print("twenty ball")

def ball():
  input("Ask me question \n")
  print(random.choice(answers))
  ball()
ball()
