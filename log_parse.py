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
		path = path
		ofile = codecs.open(('%s' % path), 'r', encoding='utf-16-le')
		ofile.seek(self.offset)
		if (ofile.readlines() == []) is False:
			ofile.seek(self.offset)
			append = ofile.readlines()
			if (self.init_check == 0) is False:
				self.text = self.text + append
				for line in append:
					line = line.encode("utf-8")
					self.log_array.append(self.line_parse(line))
			else:
				self.text = append
			self.offset = ofile.tell() + 2
		ofile.close()

	def get_start(self):
		if (self.log_array[0][1] == 'EVE System') is True:
			self.log_array = self.log_array[1:len(self.log_array)]

	def init_parse(self):
		for line in self.text[12:len(self.text)]:
                        line = line.encode("utf-8")
		for line in self.text[12:len(self.text)]:
			self.log_array.append(self.line_parse(line))

	def line_parse(self, line):
		line = line
		timestamp = line[line.find('['):line.find('[')+23]
		name = line[line.find('[')+24:line.find('>')-1]
		message = line[line.find('>')+2:line.find('\r')]
		line_array = [timestamp, name, message]
		return line_array

	def log_parse(self, path):
		path = path
		self.readout(path)
		if (self.init_check == 0) is True:
			self.init_parse()
		self.get_start()
		self.init_check = 1
		time.sleep(1)
		return self.log_array
