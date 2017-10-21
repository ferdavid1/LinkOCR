#!/usr/bin/env python
import webbrowser


if request.method == 'POST':
	if request.form['submit'] == 'submit':
		webbrowser.open("https://www.google.com")
	else:
		print("error")
else:
	print('bad')
