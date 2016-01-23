#!/usr/bin/python

# This class returns file paths for a directory. Can be used for either oldest/newest file in a directory.

import os
import time
import glob

class sort(object):
	def __init__(self):
		pass

	def comp_new(self, file_list):
                self.file_list = file_list
                self.time = 0
                self.path = None
                for path in self.file_list:
                        if (os.path.getctime(path) > self.time) is True:
                                self.time = os.path.getctime(path)
                                self.path = path
                return self.path

	def comp_old(self, file_list):
		self.file_list = file_list
		self.time = 0
		self.path = None
		for path in self.file_list:
			if (os.path.getctime(path) < self.time) is True:
				self.time = os.path.getctime(path)
				self.path = path
		return self.path

	def newest(self, path, name):
		self.path = path
		self.name = name
		args = ("%s%s" % (path, name))
		file_list = glob.glob(args)
		return self.comp_new(file_list)
	
	def oldest(self, path, name):
		self.path = path
		self.name = name
		args = ("%s%s" % (path, name))
		file_list = glob.glob(args)
		return self.comp_old(file_list)
