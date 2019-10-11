def load_stop_words(): 
	stopwords_set = set()
	with open('stopwords.txt', 'r') as stopwords:
		for word in stopwords:
			stopwords_set.add(word.rstrip("\n"))
	return stopwords_set