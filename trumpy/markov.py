import random

class MarkovChain(object):

  def __init__(self):
    self.chain = {}
    self.words = []

  def generate_chain(self, words):
    self.words = words
    if(len(words) < 3):
      return
    else:
      for i in range(len(words) - 2):
        key = (words[i], words[i+1])
        if key in self.chain:
          self.chain[key].append(words[i + 2])
        else:
          self.chain[key] = [words[i+2]]


  def generate_text(self, length):
    root = random.randint(0, len(self.words) - 2)
    w1, w2 = self.words[root], self.words[root+1]
    words = []
    for i in xrange(length):
      words.append(w1)
      w1, w2 = w2, random.choice(self.chain[(w1, w2)])
    words.append(w2)
    return ' '.join(words)