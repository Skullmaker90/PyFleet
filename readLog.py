#!/usr/bin/python

import codecs

class log(object):
	def __init__(self, path):
		self.log = []
		self.offset = 0
		self.path = path

	def acheck(self, ofile):
		ofile = ofile
		ofile.seek(self.offset)
		x = (ofile.readlines() == [])
		ofile.seek(self.offset)
		return x

	def append(self):
		with codecs.open(self.path, 'r', encoding=('utf-16-le')) as ofile:
			if self.acheck(ofile) is False:
				self.log = self.log + ofile.readlines()
				self.offset = self.offset + ofile.tell() + 2
		self.log
