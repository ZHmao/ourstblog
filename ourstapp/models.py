# -*- coding: utf-8 -*-

from django.db import models


class Author(models.Model):
	name = models.CharField(max_length=20)
	password = models.CharField(max_length=50)
	email = models.EmailField()

	def __unicode__(self):
		return '{}'.format(self.name)

class Article(models.Model):
	"""
	title:----------------����
	abstract:-------------ժҪ
	content:--------------��������
	create_date:----------����ʱ��
	modify_date:----------��һ���޸�ʱ��
	post_date:------------����ʱ��
	author:---------------����
	state:----------------״̬(0:δ������1:�ѷ�����2:ɾ��)
	"""
	title = models.CharField(max_length=50)
	abstract = models.CharField(max_length=200)
	content = models.TextField()
	create_date = models.DateTimeField(auto_now_add=True)
	modify_date = models.DateTimeField(auto_now=True)
	post_date = models.DateField()
	author = models.ForeignKey(Author)
	state = models.IntegerField()

	def __unicode__(self):
		return '{}'.format(self.title)