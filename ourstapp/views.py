# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from ourst import settings
import mistune
import os
import datetime
from django.core.mail import send_mail
from ourstapp.models import Article, Author
from ourstapp.forms import UploadForm
from django.core.context_processors import csrf


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
	article_list = Article.objects.all()
	context_dict = {'article_list': article_list}
	return render_to_response('index.html', context_dict)

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

def upload_article(req):
	new_form = UploadForm(req.POST, req.FILES)
	author = Author.objects.all()[0]
	if req.method == 'POST' and new_form.is_valid():
		raw_file = req.FILES['md_file']
		content = raw_file.read()
		content = content.decode('utf-8')
		content = mistune.markdown(content)
		new_article = Article(title=new_form.cleaned_data['title'], abstract=new_form.cleaned_data['abstract'], content=content , post_date=datetime.date.today(), author=author, state=1)
		new_article.save()
	
	my_context = {'form': UploadForm(), 'user': req.user}
	my_context.update(csrf(req))
	return render_to_response('upload.html', my_context)


# send email
def send_to_me(req):
	form_content = {'subject': 'A contact'}
	if req.method == 'GET':
		pass
	elif req.method == 'POST':
		form_content['name'] = req.META.get('name', 'None')
		form_content['email'] = req.META.get('email', 'None')
		form_content['phone'] = req.META.get('phone', 'None')
		form_content['msg'] = req.META.get('message', 'None')

	subject = 'test'
	main_msg = 'this is ourst test'
	from_email = '841923148@qq.com'
	send_mail(form_content['subject'], form_content['name']+': '+form_content['msg']+', phone: '+form_content['phone'], form_content['email'], ['ourstmao@gmail.com'])
	return HttpResponse('Thanks! I will read it .')