#! /usr/bin/env python

import commands
import urllib
import sys

class Tools:
	"""
	Generic tools class for use over IM
	"""
	def __init__(self):
		data = sys.argv[1:]

		method = data[0]

		try:
			self.line = data[1]
		except:
			pass

		self.dispatch = {
			"uptime" : self.uptime,
		}
		
		try:
			self.dispatch[method]()
		except:
			pass	

	def uptime(self):
		"""
		Return the output from uptime
		"""
		print commands.getoutput("uptime")

if __name__ == "__main__":
	Tools()