def load_stop_words(): 
	stopwords_set = set()
	with open('stopwords.txt', 'r') as stopwords:
		for word in stopwords:
			stopwords_set.add(word)
	return stopwords_set