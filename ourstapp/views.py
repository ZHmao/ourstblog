# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.

title_dict = {
	'useMD': u'Markdown 初次使用经历',
	'oracleOP': u'常用的Oracle数据库操作'
	}
preview_dict = {
	'useMD': u'我相信，一百个完美的计划也比不上一次失败的尝试。',
	'oracleOP': u'数据库是信息爆炸时代发展的坚实基础。'
	}

def homepage1(req):
    return HttpResponse('what')

def homepage(req):
    return render_to_response('index.html')

def contact(req):
	return render_to_response('contact.html')

def about(req):
	return render_to_response('about.html')

def post(req, file_name):
	my_context_dict = {
		'article_title': title_dict['file_name'],
		'article_preview': preview_dict['file_name']
		}
	return render_to_response('post.html', mycontext_dict)
