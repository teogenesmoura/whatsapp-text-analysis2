class Conversation:
	freqAnalysis, stopwords, Iramuteq = False, False, False
	def __init__(self, arguments, file):
		self.freqAnalysis = True if arguments['freqAnalysis'] else False 
		self.stopwords = True if arguments['stopwords'] else False 
		self.Iramuteq = True if arguments['Iramuteq'] else False 
		self.file = file