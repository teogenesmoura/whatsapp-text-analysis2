import unittest, os
from InputHandler import WhatsappConversationAnalysis

class TestFreqAnalysis(unittest.TestCase):
	
	@classmethod
	def setUpClass(self):
		self.sample_general_text = open("sample_general_text.txt", "r").read()
		self.w = WhatsappConversationAnalysis()
		self.freq_result_general_text = self.w._freq_analysis(self.sample_general_text)

	def test_freq_analysis(self):
		empty_text = self.w._freq_analysis("")
		self.assertEqual(empty_text, "please input a body of text in order to run the frequency analysis")
		self.assertTrue(isinstance(self.freq_result_general_text, dict))
		self.assertTrue(len(self.freq_result_general_text) > 0)

	def test_save_freq_to_csv(self):
		self.w._save_freq_to_csv(self.freq_result_general_text)
		self.assertTrue(os.stat("freq.csv").st_size != 0)		

if __name__ == '__main__':
	unittest.main()