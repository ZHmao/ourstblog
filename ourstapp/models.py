# -*- coding: utf-8 -*-

from django.db import models


class Article(models.Model):
	"""
	title:----------------标题
	abstract:-------------摘要
	content:--------------主体内容
	create_date:----------创建时间
	modify_date:----------上一次修改时间
	post_date:------------发布时间
	author:---------------作者
	state:----------------状态(0:未发布；1:已发布；2:删除)
	"""
	title = models.CharField(max_length=50)
	abstract = models.CharField(max_length=200)
	content = models.TextField()
	create_date = models.DateTimeField(auto_now_add=True)
	modify_date = models.DateTimeField(auto_now=True)
	post_date = models.DateField()
	author = models.ForeignKey(Author)
	state = models.IntegerField()

class Author(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField()
