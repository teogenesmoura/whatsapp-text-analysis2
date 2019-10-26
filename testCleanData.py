import unittest, os
from InputHandler import WhatsappConversationAnalysis
from util import remove_words_shorter_than_2,remove_wpp_telephone_number_and_time

class TestFreqAnalysis(unittest.TestCase):
	
	@classmethod
	def setUpClass(self):
		self.sample_general_text = open("sample_general_text.txt", "r").read()
		self.w = WhatsappConversationAnalysis()

	def test_remove_words_shorter_than_2(self):
		lines = ["aaa", "a", "aa"]
		self.assertEqual(remove_words_shorter_than_2(lines), ['aaa', '', ''])	

	def test_remove_wpp_telephone_number_and_time(self):
		conversation_line = ["[10/09/2019 20:47:30] ‪+55 94 9141‑5888‬: Agora sim vamos nessa."]
		expected = ["Agora sim vamos nessa."]
		self.assertEqual(remove_wpp_telephone_number_and_time(conversation_line), expected)


if __name__ == '__main__':
	unittest.main()