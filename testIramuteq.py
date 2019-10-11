import unittest
from InputHandler import WhatsappConversationAnalysis
from util import load_stop_words

class TestStopWords(unittest.TestCase):

	def test_load_stopwords(self):
		stopwords = load_stop_words()
		sample_word = list(stopwords)[0]
		self.assertTrue("\n" not in sample_word)
		self.assertTrue(isinstance(stopwords, set))

	def test_stopwords(self):
		w = WhatsappConversationAnalysis() 
		only_contains_sw = "ele como mas ao"
		doesnt_contain_sw = "futebol mágica quadro"
		has_both = "ele futebol mágica"
		result_only_contains_sw = kw._remove_stop_words(only_contains_sw)
		result_doesnt_contain_sw = w._remove_stop_words(doesnt_contain_sw)
		result_has_both = w._remove_stop_words(has_both)
		self.assertEqual(len(result_only_contains_sw),0,"only_contains_sw fails")

if __name__ == '__main__':
    unittest.main()