#!/usr/bin/python

# This class is used to open utf-16-le text documents and parse them accodingly.

import os, codecs

class log_parse(object):
	def __init__(self):
		self.text = []
		self.log_array = []
		self.offset = 0

	def readout(self, path):
		self.path = path
		self.ofile = codecs.open(('%s' % self.path), 'r', encoding='utf-16-le')
		self.ofile.seek(self.offset)
		if (self.ofile.readlines() == []) is False:
			self.ofile.seek(self.offset)
			self.text = self.text + self.ofile.readlines()
			self.offset = self.ofile.tell()
			self.ofile.close()

	def line_parse(self, line):
		self.line = line
		self.timestamp = self.line[1:24]
		self.name = self.line[25:self.line.find('>')-2]
		self.message = self.line[self.line.find('>')+2:self.line.find('\r')]
		self.line_array = [self.timestamp, self.name, self.message]
		return self.line_array

	def log_parse(self, path):
		self.path = path
		self.readout(self.path)
		self.text = self.text[13:len(self.text)]
		for line in self.text:
			line = line.encode('utf-8')
		for line in self.text:
			self.log_array.append(self.line_parse(line))
		return self.log_array

