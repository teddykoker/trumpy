from trumpy.bot import Bot

import config

import unittest
import os

class TestTrumpy(unittest.TestCase):
  def setUp(self):
    print "SETUP!"

  def test_basic(self):
    self.bot = Bot(config.TOKEN, config.TOKEN_KEY, config.CONSUMER_KEY, config.CONSUMER_SECRET);

    file_ = open(os.path.realpath("data1.txt"))
    self.bot.read_speech(file_)
    self.bot.post()

if __name__ == '__main__':
  unittest.main()
