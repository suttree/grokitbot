#!/usr/bin/env python

from reverend.thomas import Bayes

class AIMLBayes(Bayes):
  """
  Just a wrapper around the Reverend Bayes parser.
  
  Duncan Gough 13/03/04
  
  - Updated to create a Bayes file if one doesn't exist at startup.
  
  Duncan Gough 11/01/09
  """
  def __init__(self,name):
    Bayes.__init__(self)

    self.brain = name + '.bay'

    try:
      Bayes.load(self,self.brain)
      print "[Bayes] Brain loaded ok"
    except:
      print "[Alert] Failed to load bayesian brain - %s, creating it now" % self.brain
      Bayes.save(self,self.brain)
      Bayes.load(self,self.brain)

  def train(self,bucket,words):
    """
    Nominate a bucket to which the words apply, and train accordingly
    """
    if bucket != "" and words != "":
      try:
        Bayes.train(self,bucket,words)
        Bayes.save(self,self.brain)
      except:
        print "Failed to learn"
    else:
      return None

  def untrain(self,bucket,words):
    """
    Remove nominated words from the relevant bucket
    """
    Bayes.untrain(self,bucket,words)
    Bayes.save(self,self.brain)

  def guess(self,line):
    """
    Guess what category these words apply to
    """
    #print Bayes.guess(self,line)
    return Bayes.guess(self,line)
  
  def forget(self):
    pass

  def save(self):
    """
    Save the brain to disk
    """
    Bayes.save(self,self.brain)

if __name__ == "__main__":
  AIMLBayes()