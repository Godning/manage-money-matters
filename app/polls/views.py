from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .forms import Person_form
from polls.models import Person,Mouth,Details

# Create your views here.

def login(request):
	if request.method == 'POST':
		form = Person_form(request.POST)

		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			person = Person.objects.filter(username=username,password=password)
			results = {}
			results['success'] = False
			results['reason'] = 'username or password error'
			if person:
				request.session['username'] = username
				results['success'] = True
				results['reason'] = 'login success'
				return JsonResponse(results)
			else:
				return JsonResponse(results)
	return render(request,'polls/login.html')

def search(request):
	if request.method == 'POST':
		search_mouth = request.POST['search_mouth']
		username = request.session['username']
		if username:
			person = Person.objects.get(username=username)
			mouth = Mouth.objects.get(person=person,mouth=search_mouth)
			details = Details.objects.get(mouth=mouth)
			if mouth:
				resluts = {}
				resluts['mouth'] = details.mouth.mouth
				resluts['day'] = details.day
				resluts['remarks'] = details.remarks
				resluts['cost'] = details.cost
				return JsonResponse(resluts)
		return render(request,'polls/login.html')
	return render(request,'polls/search.html')
