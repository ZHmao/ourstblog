# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.

title_dict = {
	'useMD': u'Markdown ����ʹ�þ���',
	'oracleOP': u'���õ�Oracle���ݿ����'
	}
preview_dict = {
	'useMD': u'�����ţ�һ�ٸ������ļƻ�Ҳ�Ȳ���һ��ʧ�ܵĳ��ԡ�',
	'oracleOP': u'���ݿ�����Ϣ��ըʱ����չ�ļ�ʵ������'
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
