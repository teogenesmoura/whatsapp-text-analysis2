import unittest
from InputHandler import WhatsappConversationAnalysis
from util import load_stop_words

class TestStopWords(unittest.TestCase):

	def test_load_stopwords(self):
		stopwords = load_stop_words()
		sample_word = list(stopwords)[0]
		random_words = set(['que', 'para', 'por', 'na']) 
		self.assertTrue("\n" not in sample_word)
		self.assertTrue(isinstance(stopwords, set))
		self.assertTrue(len(stopwords) > 0)
		self.assertTrue(random_words.issubset(stopwords)) #checks if at least some of the expected words are loaded

	def test_remove_stop_words(self):
		stopwords = load_stop_words()
		w = WhatsappConversationAnalysis()
		word = ["que", "para", "por", "na"]
		self.assertTrue(len(w._remove_stop_words(word)) == 0)
		self.assertTrue(len(w._remove_stop_words(stopwords)) == 0)

if __name__ == '__main__':
    unittest.main()