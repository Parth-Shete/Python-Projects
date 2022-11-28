from chatterbot.chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

my_bot = ChatBot(
    name = "PyBot",
    read_only = True,
    logic_adaptors = ["chatterbot.logic.MathematicalEvaluation", "chatterbot.logic.BestMatch"]
)

small_talk = [
    'hi there!',
    'hi!',
    'how do you do?',
    'how are you?',
    'i am cool',
    'fine, you?',
    'always cool.',
    'i am okay',
    'glad to hear that.',
    'i am fine',
    'i feel awesome',
    'excellent, glad to hear that.',
    'not so good',
    'sorry to hear that.',
    'what is your name?',
    'i am pybot. ask me a math question, please.',
]

math_talk_1 = [
    'python theorem',
    'a squared plus b squared equals c squared.',
]

math_talk_2 = [
    'law of cosines',
    'c**2 = a**2 + b**2 - 2*a*b*cos(gamma)',
]

list_trainer = ListTrainer(my_bot)

for item in (small_talk, math_talk_1, math_talk_2):
    list_trainer.train(item)

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')

print(my_bot.get_response("hi"))

print(my_bot.get_response("i feel awesome today!"))

print(my_bot.get_response("what's your name?"))

print(my_bot.get_response("show me pythagores theorem"))

print(my_bot.get_response("do you know the law of cosines?"))

while True:
    try:
        bot_input = input("You: ")
        bot_response = my_bot.get_response(bot_input)
        print(f"{my_bot.name}: {bot_response}")
    except (KeyboardInterrupt, EOFError, SystemExit):
        break;