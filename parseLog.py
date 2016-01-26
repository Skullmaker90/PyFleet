#!/usr/bin/python

# This class is used to open utf-16-le text documents and parse them accodingly.

import os, codecs, time

class log_parse(object):
	def __init__(self):
		self.text = []
		self.log_array = []
		self.lolen = 0
		self.tlen = 0

	def cut_log(self):
		if (self.log_array[0][1] == 'EVE System') is True:
			self.log_array = self.log_array[13:len(self.log_array)]

	def line_parse(self, line):
		line = line
		timestamp = line[line.find('['):line.find('[')+23]
		name = line[line.find('[')+24:line.find('>')-1]
		message = line[line.find('>')+2:line.find('\r')]
		line_array = [timestamp, name, message]
		return line_array

	def log_parse(self, text):
		for line in text:
			line = self.line_parse(line)
			self.log_array.append(line)
		get_log()
		return self.log_array
