#!/usr/bin/python

# This class is used to post to slack.

import os, json

class slack_post(object):
	def __init__(self):
		self.hook = None
		self.payload = {}

	def get_hook(self):
		a = open("./slack_hook")
		self.hook = a.read()

	def format_payload(self, line):
		self.payload['channel'] = "#talitest"
		self.payload['username'] = "Fleet Bot"
		self.payload['text'] = ("%s:\n%s\nTimestamp: %s" % (line[1], line[2][4:len(line[2])], line[0]))

	def slack_post(self, line):
		self.get_hook()
		self.format_payload(line)
		try:
			print(self.payload)
			print(self.hook)
			os.system("curl -X POST --data-urlencode 'payload=%s' %s" % (json.dumps(self.payload), self.hook))
			print("Ok")
		except:
			raise

