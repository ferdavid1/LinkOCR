#!/usr/bin/env python
from django.http import HttpResponse
from demo import main

def open(request):

	site = main()
	html = "<html><body><a href={}/></body></html>".format(site)

	return HttpResponse(html)
