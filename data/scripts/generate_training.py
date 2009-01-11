#! /usr/bin/env python

from string import join, upper

import sys

def main():
	"""
	Really simple/hacky way of generating an aiml file
	that can be learnt and used to train the bot.
	"""
	data = sys.argv[1:]
	meaning = data[1].upper()
	
	xml = ['<aiml>']
	
	xml.append('<topic name="TRAINING%s">' % data[0].upper())

	xml.append('<category>')
	xml.append('<pattern>%s MEANS *</pattern>' % meaning)
	xml.append('<template>')
	xml.append('<star/>')
	xml.append('</template>')
	xml.append('</category>')
	
	xml.append('<category>')
	xml.append('<pattern>IT MEANS *</pattern>')
	xml.append('<template>')
	xml.append('<star/>')
	xml.append('</template>')
	xml.append('</category>')
	
	# Training get out clauses
	xml.append('<category>')
	xml.append('<pattern>NEVER MIND</pattern>')
	xml.append('<template>')
	xml.append('NEVERMIND')
	xml.append('</template>')
	xml.append('</category>')

	xml.append('<category>')
	xml.append('<pattern>NEVERMIND</pattern>')
	xml.append('<template>')
	xml.append('NEVERMIND')
	xml.append('</template>')
	xml.append('</category>')

	# Catchall
	xml.append('<category>')
	xml.append('<pattern>*</pattern>')
	xml.append('<template>')
	xml.append('<star/>')
	xml.append('</template>')
	xml.append('</category>')

	xml.append('</topic>')
	
	xml.append('</aiml>')
	
	str = join(xml,'\n')
	
	f = open("./data/aiml/training/" + data[0] + ".aiml", "w")
	f.write(str)
	f.close()

if __name__ == "__main__":
    main()