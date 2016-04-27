from django import forms

class Person_form(forms.Form):
	username = forms.CharField(max_length=15)
	password = forms.CharField(max_length=20)

class Search_mouth(forms.Form):
	search_mouth = forms.IntegerField()