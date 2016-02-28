from twitter import *
from . import markov

class Bot(object):

  def __init__(self, token, token_key, con_secret, con_secret_key):
    self.twitter = Twitter(auth=OAuth(token, token_key, con_secret, con_secret_key))
    self.chain = markov.MarkovChain()

  def read_speech(self, open_file):
    open_file.seek(0)
    data = open_file.read()
    words = data.split()
    self.chain.generate_chain(words)

  def post(self, length=32):
    text = self.chain.generate_text(length)
    text = text[:140]

    while text.rfind('.') == -1: # while the text has no periods generate new text
      text = self.chain.generate_text(length)
      text = text[:140]

    text = text[:text.rfind('.') + 1] #  cut text down until it ends at a period
    text = text[0].upper() + text[1:]

    print text
    self.twitter.statuses.update(status = text) #post text
