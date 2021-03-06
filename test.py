from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

chatbot = ChatBot('Will Li')
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.corpus.english")
chatbot.set_trainer(ListTrainer)

fh = open('sample_data.txt')
lines = [line.rstrip('\n') for line in fh]
fh.close()

for x in range(0,5):
    chatbot.train(lines[(3*x):(3*x+1)])

print(chatbot.get_response('Where can I find my test'))
