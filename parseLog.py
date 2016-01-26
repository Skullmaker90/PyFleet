#!/usr/bin/python

# This class is used to open utf-16-le text documents and parse them accodingly.

def line_parse(self, line):
	line = line.encode('utf-8')
	timestamp = line[line.find('['):line.find('[')+23]
	name = line[line.find('[')+24:line.find('>')-1]
	message = line[line.find('>')+2:line.find('\r')]
	line_array = [timestamp, name, message]
	return line_array

def log_parse(self, log):
	text = text
	log = []
	for line in log:
		line = line_parse(line)
		log.append(line)
	if (log[0][12] == 'EVE System') is True:
		log = log[13:len(log)]
	return log
