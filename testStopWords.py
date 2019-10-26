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

if __name__ == '__main__':
    unittest.main()