#!/usr/bin/env python

from twisted.words.protocols import irc
from twisted.internet import protocol
from twisted.internet import reactor
from AIMLBot import AIMLBot
import sys
import re

class GrokItBot(irc.IRCClient):
  """
  An AIM bot that uses both PyAIML and Reverend Bayes 
  parser to learn and respond to messages.
  
  Duncan Gough 13/03/04
  
  - Updated to switch form TocTalk/AIM to Twisted/IRC
  
  Duncan Gough 11/01/09
  
  PyAIML: http://pyaiml.sourceforge.net/
  Reverend Bayes: http://www.divmod.org/Home/Projects/Reverend/
  Twisted: http://twistedmatrix.com/
  
  GrokItBot: http://www.suttree.com/code/grokitbot/
  """
  def _get_nickname(self):
    return self.factory.nickname
  nickname = property(_get_nickname)

  def signedOn(self):
    self.join(self.factory.channel, self.factory.password)
    print "Signed on as %s." % (self.nickname,)

  def joined(self, channel):
    print "Joined %s." % (channel,)

  def privmsg(self, user, channel, msg):
    if msg.startswith('*** '):
      print msg
      return
    elif not user:
      return
    elif self.nickname in msg:
      msg = re.compile(self.nickname + "[:,]* ?", re.I).sub('', msg)
      prefix = "%s: " % (user.split('!', 1)[0], )
    else:
      prefix = ''

    sentence = self.factory.aiml.on_MSG_IN(user.split('!', 1)[0],msg)
    self.msg(self.factory.channel, prefix + sentence)

class GrokItBotFactory(protocol.ClientFactory):
  protocol = GrokItBot

  def __init__(self, channel, nickname, password=''):
    self.channel = channel
    self.nickname = nickname
    self.password = password
    self.aiml = AIMLBot(self.nickname)

  def clientConnectionLost(self, connector, reason):
    print "Lost connection (%s), reconnecting." % (reason,)
    connector.connect()

  def clientConnectionFailed(self, connector, reason):
    print "Could not connect: %s" % (reason,)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    nickname = sys.argv[1]
    channel = sys.argv[2]
    password = sys.argv[3]
  else:
    nickname = 'GrokItBot'
    channel = 'suttree.com'
    password = ''

  reactor.connectTCP('irc.pmog.com', 6667, GrokItBotFactory('#' + channel, nickname, password))
  reactor.run()