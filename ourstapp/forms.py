# -*- coding: utf-8 -*-

from django import forms

class UploadForm(forms.Form):
	title = forms.CharField(label='Title:')
	abstract = forms.CharField(label='Abstract:')
	md_file = forms.FileField()