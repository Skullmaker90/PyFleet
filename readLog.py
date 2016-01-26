#!/usr/bin/python

class log(object):
	def __init__(self, path):
		self.log = None
		self.ofile = None
		self.path = path
		self.offset = 0

	def open(self):
		try:
			self.ofile = codecs.open(('%s' % self.path), 'r', encoding='utf-16-le')
		except IOError:
			print("Could not open file.")
			
	def acheck(self):
		self.ofile.seek(self.offset)
		x = (self.ofile.readlines() == [])
		self.ofile.seek(self.offset)
		return x

	def append(self):
		if self.acheck() is False:
			self.log = self.log + self.ofile.readlines()
			self.offset = self.offset + self.ofile.tell() + 2
		return self.log
