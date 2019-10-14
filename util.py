def load_stop_words(): 
	stopwords_set = set()
	with open('stopwords.txt', 'r') as stopwords:
		for word in stopwords:
			stopwords_set.add(word.rstrip("\n"))
	return stopwords_set

def load_Iramuteq(columnsOption):
	iramuteq_file = open("iramuteq_lexicon.txt", "r")
	iramuteq_map = dict()
	for line in iramuteq_file.readlines():
		current = line.split("	")
		try:
			if columnsOption == "word-equivalent":
				iramuteq_map[current[0]] = current[1]
			if columnsOption == "equivalent-grammarcategory":
				iramuteq_map[current[0]] = current[2]
		except:
			print("error ocurred while importing iramuteq from text file")
	iramuteq_file.close()
	return iramuteq_map