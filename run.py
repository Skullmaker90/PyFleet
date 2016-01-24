#!/usr/bin/python

import os, time
import dir_sort, log_parse, key_watch, slack_post

def main(a, b, c, d):
        x = a.newest("/win7/", "Alliance*")
	print(x)
        while True:
		try:
                	y = b.log_parse(x)
			print(y)
                	z = c.key_watch(y, "!fb")
			print(z)
			if z is not None:
				d.slack_post(z)
                	time.sleep(1)
		except KeyboardInterrupt:
			print("\nCaught SIGTERM, Cleaning Up.")
			break

def __init__():
	a = dir_sort.sort()
	b = log_parse.log_parse()
	c = key_watch.key_watch()
	d = slack_post.slack_post()
	main(a, b, c, d)

__init__()
