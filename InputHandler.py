from Conversation import Conversation
import FreqHandler 

class InputHandler:
	def loadFileFromDisk(self, filePath):
		try:
			f = open(filePath, "r")			
			return f.read()
		except IOError:
			print("Error while opening file")
			return 0

class Dispatcher:
	def __init__(self, arguments):
		self.file = InputHandler.loadFileFromDisk(self,arguments['<textfile>'])
		print(self.file)
		# convObject = Conversation(arguments, self.file)
		# self.callHandler(convObject)



