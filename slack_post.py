#!/usr/bin/python

# The class is used to connect and post to slack after formatting a payload.

import os, json

class slack_post(object):
	def ___init__(self):
		self.hook = None
		self.payload = {}

	def format_payload(self, line):
		self.payload['channel'] = "#talitest"
		self.payload['username'] = "Fleet Bot"
		self.payload['text'] = ("%s:\n%s\nTimestamp: %s" % (line[1], line[2][4:len(line[2])], line[0]))
		json.dump(self.payload)

	def get_hook(self):
		a = open("./slack_hook")
		self.hook = a.read()

	def slack_post(self, line):
		self.get_hook()
		self.format_payload(line)
		os.system("curl -X POST --data-urlencode 'payload='%s' %s" % (self.payload, self.hook))
