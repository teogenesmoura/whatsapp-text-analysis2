<<<<<<< HEAD
"""Usage:
  wppAnalysis.py run <textfile> [--freqAnalysis=<freqAnalysis>] [--stopwords=<stopWords>] [--Iramuteq=<Iramuteq>]
"""
from docopt import docopt
from util import load_stop_words
import abc,re

class AbstractClass(metaclass=abc.ABCMeta):
=======
import abc, re

class AbstractClass():
>>>>>>> 7083baabfd8af37f62c0e787900d8239b106a446

	def execution_steps(self, conversationPath):
		self.conversation_body_of_text = self._load_input(conversationPath)
		self.conversation_body_of_text = self._clean_data(self.conversation_body_of_text)
		self.conversation_body_of_text = self._remove_stop_words(self.conversation_body_of_text)
		self.conversation_body_of_text = self._apply_Iramuteq(self.conversation_body_of_text)
		self.conversation_body_of_text = self._freq_analysis(self.conversation_body_of_text)
		return self.conversation_body_of_text

	@abc.abstractmethod
	def _load_input(conversationPath):
		pass

	@abc.abstractmethod
	def _clean_data(conversationPath):
		pass

	@abc.abstractmethod
	def _remove_stop_words(conversationBodyOfText):
		pass

	@abc.abstractmethod
	def _apply_Iramuteq(conversationBodyOfText):
		pass

	@abc.abstractmethod
	def _freq_analysis(conversationBodyOfText):
		pass 

class WhatsappConversationAnalysis(AbstractClass):

	def _load_input(self, conversationPath):
		return open(conversationPath, 'r').read()

	def _clean_data(self, conversation):
		regex_info_message = r"\[.*?\].{3,4}\d{2}.\d{2}.\d{4,5}.\d{4}.:*"
		lines = conversation.splitlines()
		result = ""
		for line in lines:
			line = line.strip()
			if line:
<<<<<<< HEAD
				result += re.sub(regex_info_message, "", line.lower()) + "\n"
		return result

	def _remove_stop_words(self, conversation):
		stop_words = load_stop_words()
		result = ""
		for word in conversation.split():
			if word not in stop_words:
				result += word + " "
		return result
=======
				result += re.sub(regex_info_message, "", line) + "\n"
				print(result)
		return result 

	def _remove_stop_words(self, conversation):
		pass
>>>>>>> 7083baabfd8af37f62c0e787900d8239b106a446

	def _apply_Iramuteq(self, conversation):
		pass 

	def _freq_analysis(self, conversation):
		pass

def Init(arguments):
	Wpp = WhatsappConversationAnalysis()
	Wpp.execution_steps(arguments['<textfile>'])

<<<<<<< HEAD
if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1.1rc')
    if arguments['<textfile>']:
    	Init(arguments)
    else: 
    	print("You should input a textfile")
=======
if __name__ == "__main__":
	main()
>>>>>>> 7083baabfd8af37f62c0e787900d8239b106a446
