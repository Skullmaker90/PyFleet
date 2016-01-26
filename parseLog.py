#!/usr/bin/python

# This class is used to open utf-16-le text documents and parse them accodingly.

def line_parse(line):
	line = line.encode('utf-8')
	timestamp = line[line.find('['):line.find('[')+23]
	name = line[line.find('[')+24:line.find('>')-1]
	message = line[line.find('>')+2:line.find('\r')]
	line_array = [timestamp, name, message]
	return line_array

def log_parse(log):
	text = log
	log = []
	for line in text:
		line = line_parse(line)
		log.append(line)
	if (log[12][2] != 'EVE System') is False:
		log = log[12:len(log)]
		return log
	log = log[13:len(log)]
	return log
