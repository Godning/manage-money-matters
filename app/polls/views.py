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
		results = {}
		results['success'] = False
		if 'username' in request.session:
			print('memeda')
			username = request.session['username']
			person = Person.objects.get(username=username)
			mouth = Mouth.objects.get(person=person,mouth=search_mouth)
			details = Details.objects.get(mouth=mouth)
			if mouth:
				print('heihei')
				results['success'] = True
				results['mouth'] = details.mouth.mouth
				results['day'] = details.day
				results['remarks'] = details.remarks
				results['cost'] = details.cost
				return JsonResponse(results)
		else:
			print('hhh')
			return JsonResponse(results)
	return render(request,'polls/search.html')

def details(request):
	if request.method == 'POST':
		username = request.session['username']
		if username:
			person = Person.objects.get(username=username)
			mouth = Mouth.objects.get(person=person)
			details = Details.objects.get(mouth=mouth)
			day = request.POST['day_input']
			cost = request.POST['cost_input']
			remarks = request.POST['remarks_input']
			#mouth.residu = mouth.residu-cost




