from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .forms import Person_form,Search_mouth
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
		form = Search_mouth(request.POST)
		results = {}
		results['success'] = False
		results['data'] = False
		results['login'] = False
		if 'username' in request.session:
			search_mouth = request.POST['search_mouth']
			results['login'] = True
			if form.is_valid():
				print('memeda')
				username = request.session['username']
				person = Person.objects.filter(username=username)
				mouth = Mouth.objects.filter(person=person,mouth=search_mouth)
				details = Details.objects.filter(mouth=mouth)
				results['success'] = True
				if mouth:
					results['data'] = True
					results['mouth'] = details[0].mouth.mouth
					results['day'] = details[0].day
					results['remarks'] = details[0].remarks
					results['cost'] = details[0].cost
					results['residu'] = mouth[0].residu
					return JsonResponse(results)
				else:
					results['data'] = False
					results['back'] = 'have no this data'
					return JsonResponse(results)
			else:
				results['back'] = 'please input integer'
				return JsonResponse(results)
		else:
			return JsonResponse(results)
	return render(request,'polls/search.html')


def center(request):
	if request.method == 'POST':
		if 'username' in request.session:
			username = request.session['username']
			person = Person.objects.get(username=username)
			mouths = Mouth.objects.filter(person=person)
			mouth = mouths[0]
			# details = Details.objects.get(mouth=mouth)
			day = request.POST['day']
			cost = request.POST['cost']
			remarks = request.POST['remarks']
			details = Details(day=day,cost=cost,remarks=remarks,mouth=mouth)
			mouth.residu = str(int(float(mouth.residu)-float(cost)))
			details.save()
			mouth.save()
			results = {}
			results['success'] = True
		return JsonResponse(results)
	return render(request,'polls/user_center.html')




