"""Usage:
  wppAnalysis.py run <textfile> [--freqAnalysis=<freqAnalysis>] [--stopwords=<stopWords>] [--Iramuteq=<Iramuteq>]
"""
from docopt import docopt
from InputHandler import Init
<<<<<<< HEAD
=======
import abc
>>>>>>> 7083baabfd8af37f62c0e787900d8239b106a446

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1.1rc')
    if arguments['<textfile>']:
    	Init(arguments)
    else: 
    	print("You should input a textfile")