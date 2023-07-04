from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

cb = ChatBot('test')
lt = ListTrainer(cb)
lt.train(["Hello", "Hi there!", "Pangit mo", "Ako kasi si malena"])

r = cb.get_response('Pangit mo')
print(r)