import re, emoji, string 

def lowercase(conversation):
	return [line.lower() for line in conversation]

def remove_punctuation(conversation):
	return [line.translate(str.maketrans('', '', string.punctuation)) for line in conversation]

def remove_emojis(lines):
	for line in lines:
		line = extract_emojis(line)
	return lines

def extract_emojis(str):
	return ''.join(c for c in str if c not in emoji.UNICODE_EMOJI)

def remove_wpp_telephone_number_and_time(lines):
	return [re.sub(r"\[.*?\].{3,4}\d{2}.\d{2}.\d{4,5}.\d{4}.:*", "", line) for line in lines]	

def remove_words_shorter_than_2(lines):
	return [re.sub(r"\b\w{1,2}\b", "", line) for line in lines]

def load_stop_words(): 
	file = open('stopwords.txt', 'r')
	stopwords = set(line.strip() for line in file)
	file.close()
	return stopwords

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