# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse
from ourst import settings
import mistune
import os

# Create your views here.

title_dict = {
	'useMD': 'Be Confidence',
	'oracleOP': 'Be Confidence'
	}
preview_dict = {
	'useMD': '',
	'oracleOP': ''
	}

def homepage1(req):
    return HttpResponse('what')

def homepage(req):
    return render_to_response('index.html')

def contact(req):
	return render_to_response('contact.html')

def about(req):
	return render_to_response('about.html')

def undev(req):
	return render_to_response('undev.html')

def blog(req, file_name):
	content = 'no content'
	file_path = settings.STATICFILES_DIRS[0] + 'article/' + file_name + '.md'
	if os.path.isfile(file_path):
		with open(file_path, 'r') as fr:
			content = fr.read()
			content = content.decode('utf-8')
			content = mistune.markdown(content)
	my_context_dict = {
		'article_title': title_dict[file_name],
		'article_preview': preview_dict[file_name],
		'article_content': content
		}
	return render_to_response('article.html', my_context_dict)
