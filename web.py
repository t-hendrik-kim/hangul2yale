# -*- coding: utf-8 -*-

import cgi
import hangul2yale

# Main
if __name__ == "__main__":

	form = cgi.FieldStorage()
	if form.getvalue('hangul'):
		hangul = form.getvalue('hangul').decode('utf-8')
		result = hangul2yale.convert_string(string=hangul)
	else:
		result = "No input provided. Please enter a Hangul string."
	
	print("Content-type: text/plain;charset=utf-8\n")
	print(cgi.escape(result).encode('utf-8'))
