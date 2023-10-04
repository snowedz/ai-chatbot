from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import collections.abc
collections.Hashable = collections.abc.Hashable


chatbot = ChatBot("Snowzin")
# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train("chatterbot.corpus.portuguese")

exit_conditions = ("sair","tchau","bye")


while True:
    question = input("> ")
    if question in exit_conditions:
        break
    else:
        print(f"{chatbot.name} : {chatbot.get_response(question)}")
    