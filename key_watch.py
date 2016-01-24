#!/usr/bin/python

# This class is meant to take the output of a parsed log [[timestamp1,name1,message1],[timestamp2,name2,message2]],
# and make comparisons against it. Still thinking of a way to dynamically update the tuple though.

class key_watch(object):
	def __init__(self):
		self.key = None
		self.response_line = []
		self.parsed_log = []
		self.last_line = []
		self.offset = 0

	def line_comp(self):
		self.offset = len(self.parsed_log)-1
		if (self.last_line == self.parsed_log[self.offset]) is False:
			self.last_line = self.parsed_log[self.offset]
			self.line_parse = self.parsed_log[self.offset][2]
			self.line_parse = self.line_parse.split(' ')
			if (self.key == self.line_parse[0]) is True:
				self.response_line = self.parsed_log[self.offset]
				print("Key Found! Time: %s, Name: %s, Message: %s" % (self.response_line[0], self.response_line[1], self.response_line[2]))
				return self.response_line

	def key_watch(self, parsed_log, key):
		self.key = key
		self.parsed_log = self.parsed_log + parsed_log
		return self.line_comp()
		
