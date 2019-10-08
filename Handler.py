from abc import ABC, abstractmethod
class Handler:
	def __init__(self, sucessor=None):
		self.successor = successor

	def handle(self, conversationObject):
		shouldContinue = self.shouldContinue(conversationObject)
		if shouldContinue:
			self.successor.handle(conversationObject)

	@abstractmethod 
	def shouldContinue(self, conversationObject):
		"checks if conversationObject has properties set to true"