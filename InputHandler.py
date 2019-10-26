"""Usage:
  wppAnalysis.py run <textfile> [--freqAnalysis=<freqAnalysis>] [--stopwords=<stopWords>] [--Iramuteq=<Iramuteq>]
"""
from docopt import docopt
from util import *
import abc
import re
import sys
import csv
from nltk.util import ngrams

class AbstractClass(metaclass=abc.ABCMeta):

    def execution_steps(self, conversationPath):
        self.conversation_body_of_text = self._load_input(conversationPath)
        self.conversation_body_of_text = self._clean_data(
            self.conversation_body_of_text)
        self.conversation_body_of_text = self._remove_stop_words(
            self.conversation_body_of_text)
        self.conversation_body_of_text = self._apply_Iramuteq(
            self.conversation_body_of_text)
        self.freq_analysis = self._freq_analysis(self.conversation_body_of_text)
        self._save_freq_to_csv(self.freq_analysis)
        self._generate_ngrams(self.conversation_body_of_text, 3)
        print(self._count_words(self.conversation_body_of_text))

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

    @abc.abstractmethod
    def _generate_ngrams(conversationBodyOfText, n):
        pass

    @abc.abstractmethod
    def _count_words(conversationBodyOfText):
        pass

class WhatsappConversationAnalysis(AbstractClass):

    def _load_input(self, conversationPath):      
      return open(conversationPath, "r", encoding="utf-8").read().splitlines()
      
    def _clean_data(self, conversation):
      conversation = remove_wpp_telephone_number_and_time(conversation)
      conversation = remove_words_shorter_than_2(conversation) 
      conversation = remove_emojis(conversation)
      return conversation

    def _remove_stop_words(self, conversation):
      stop_words = load_stop_words()
      return [word for word in conversation if word not in stop_words]

    def _apply_Iramuteq(self, conversation):
        if not conversation:
            return "please input a body of text in order to apply the Iramuteq filter"
            sys.exit(0)
        iramuteq_map = load_Iramuteq("word-equivalent")
        new_body_text = ""
        for word in conversation:
            if word in iramuteq_map:
                previous_value_of_word = word
                word = iramuteq_map[word]
            new_body_text += word + " "
        return new_body_text

    def _freq_analysis(self, conversation):
        if not conversation:
            return "please input a body of text in order to run the frequency analysis"
            sys.exit(0)
        freq_map = dict()
        for word in conversation.split():
            if word in freq_map:
                freq_map[word] += 1
            else:
                freq_map[word] = 1
        return freq_map

    def _save_freq_to_csv(self, freqDict):
        sorted_freqDict = sorted(freqDict.items(), key=lambda kv: -kv[1])
        with open('freq.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in sorted_freqDict:
                writer.writerow([key, value])

    def _generate_ngrams(self, s, n):
        # Convert to lowercases
        s = s.lower()
        # Break sentence in the token, remove empty tokens
        tokens = [token for token in s.split(" ") if token != ""]
        n_grams = list(ngrams(tokens, 3))
        with open("ngrams_tweets.txt", "w") as f:
            f.write('\n'.join('%s %s %s' % x for x in n_grams))
        return n_grams

    def _count_words(self, conversation):
      counter = 0
      for word in conversation.split():
        print(word)
        counter += 1
      return counter

def Init(arguments):
    Wpp = WhatsappConversationAnalysis()
    Wpp.execution_steps(arguments['<textfile>'])

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1.1rc')
    if arguments['<textfile>']:
        Init(arguments)
    else:
        print("You should input a textfile")

