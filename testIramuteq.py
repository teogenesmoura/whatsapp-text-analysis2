import unittest
from InputHandler import WhatsappConversationAnalysis
from util import load_stop_words, load_Iramuteq

class TestStopWords(unittest.TestCase):

	def test_load_Iramuteq(self):
		iramuteq = load_Iramuteq("word-equivalent")
		self.assertTrue(isinstance(iramuteq, dict))
		self.assertTrue(len(iramuteq) > 0)

	# def test_import_Iramuteq_from_text_file(self):
	# 	original_file = "cookie acústica acústicas acústico acústicos"
	# 	expected = "cookie acústico acústico acústico acústico "
	# 	w = WhatsappConversationAnalysis()
	# 	processed_file = w._apply_Iramuteq(original_file)
	# 	self.assertEqual(processed_file, expected)

	def test_empty_input_file(self):
		original_file = ""
		w = WhatsappConversationAnalysis()
		expected = "please input a body of text in order to apply the Iramuteq filter"
		processed_file = w._apply_Iramuteq(original_file)
		self.assertEqual(processed_file, expected)
		
if __name__ == '__main__':
    unittest.main()