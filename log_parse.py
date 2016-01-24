#!/usr/bin/python

# This class is used to open utf-16-le text documents and parse them accodingly.

import os, codecs, time

class log_parse(object):
	def __init__(self):
		self.text = []
		self.log_array = []
		self.offset = 0
		self.init_check = 0

	def readout(self, path):
		self.path = path
		self.ofile = codecs.open(('%s' % self.path), 'r', encoding='utf-16-le')
		self.ofile.seek(self.offset)
		if (self.ofile.readlines() == []) is False:
			self.ofile.seek(self.offset)
			self.append = self.ofile.readlines()
			if (self.init_check == 0) is False:
				self.text = self.text + self.append
				for line in self.append:
					line = line.encode("utf-8")
					self.log_array.append(self.line_parse(line))
			else:
				self.text = self.append
			self.offset = self.ofile.tell() + 2
		self.ofile.close()

	def get_start(self):
		if (self.log_array[0][1] == 'EVE System') is True:
			self.log_array = self.log_array[1:len(self.log_array)]

	def init_parse(self):
		for line in self.text[12:len(self.text)]:
                        line = line.encode("utf-8")
		for line in self.text[12:len(self.text)]:
			self.log_array.append(self.line_parse(line))

	def line_parse(self, line):
		self.line = line
		self.timestamp = self.line[self.line.find('['):self.line.find('[')+23]
		self.name = self.line[self.line.find('[')+24:self.line.find('>')-1]
		self.message = self.line[self.line.find('>')+2:self.line.find('\r')]
		self.line_array = [self.timestamp, self.name, self.message]
		return self.line_array

	def log_parse(self, path):
		self.path = path
		self.readout(self.path)
		if (self.init_check == 0) is True:
			self.init_parse()
		self.get_start()
		self.init_check = 1
		time.sleep(1)
		return self.log_array
