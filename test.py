from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

def test():
    chatbot = ChatBot('Will Li')
    chatbot.set_trainer(ChatterBotCorpusTrainer)
    chatbot.train("chatterbot.corpus.english")
    chatterbot.set_trainer(ListTrainer)

    fh = open('sample_data.txt')
    lines = [line.rstrip('\n') for line in fh]
    fh.close()

    for x in range(0,5):
        chatterbot.train(lines[x,x+1])

    print chatbot.getresponse('How can I see my test?')
