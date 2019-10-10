import abc, re

class AbstractClass():

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
				result += re.sub(regex_info_message, "", line) + "\n"
				print(result)
		return result 

	def _remove_stop_words(self, conversation):
		pass

	def _apply_Iramuteq(self, conversation):
		pass 

	def _freq_analysis(self, conversation):
		pass

def Init(arguments):
	Wpp = WhatsappConversationAnalysis()
	Wpp.execution_steps(arguments['<textfile>'])

if __name__ == "__main__":
	main()
