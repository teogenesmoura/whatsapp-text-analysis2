import unittest
from InputHandler import WhatsappConversationAnalysis

class TestFreqAnalysis(unittest.TestCase):
	
	@classmethod
	def setUpClass(self):
		self.sample_general_text = open("sample_general_text.txt", "r").read()
	
	def test_freq_analysis(self):
		w = WhatsappConversationAnalysis()
		empty_text = w._freq_analysis("")
		freq_result_general_text = w._freq_analysis(self.sample_general_text)
		self.assertEqual(empty_text, "please input a body of text in order to run the frequency analysis")
		self.assertTrue(isinstance(freq_result_general_text, dict))
		self.assertTrue(len(freq_result_general_text) > 0)

if __name__ == '__main__':
	unittest.main()