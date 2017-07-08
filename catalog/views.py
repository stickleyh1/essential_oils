from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

from catalog.models import Product, Order, Ailment

# -------------------------------------
# Page Views
# -------------------------------------
def index(request):
	context_dict={}
	context_dict['num_products'] = Product.objects.all().count()
	context_dict['num_singles'] = Product.objects.filter(isBlend=False).count()
	context_dict['num_blends'] = Product.objects.filter(isBlend=True).count()
	context_dict['num_ailments'] = Ailment.objects.all().count()
	return render(request, 'catalog/index.html', context_dict)

def search(request):
	if request.GET.get('q'):
		query = ''+request.GET.get('q')
		if query != None:
			return render(request, 'catalog/search_results.html')

	return render(request, 'catalog/search.html')

def search_results(request):
	if request.GET.get('q'):
		query = ''+request.GET.get('q')
		if query != None:
			results = []
			objs = Product.objects.filter(name__icontains=query).order_by('isBlend')
			for m in objs:
				results.append(m)
			return render(request, 'catalog/search_results.html', {"results": results,})

	return render(request, 'catalog/search.html')

class ProductListView(generic.ListView):
    model = Product

class ProductDetailView(generic.DetailView):
    model = Product

class AilmentListView(generic.ListView):
    model = Ailment

# class UserDetailView(generic.DetailView):
# 	model = User

# 	def get_context_data(self, **kwargs):
# 		context = super(UserDetailView, self).get_context_data(**kwargs)
# 		context['instances'] = MediaInstance.objects.all()
# 		context['medias'] = Media.objects.all()
# 		for i in context['instances']:
# 			if i.due_date and i.due_date < dt.date.today():
# 				i.late_fee = (dt.date.today() - i.due_date).days

# 		return context

# -------------------------------------
# User Authentication
# -------------------------------------
def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)

		if user_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print(user_form.errors)
	else:
		user_form = UserForm()

	return render(request, 'rango/register.html',
		{'user_form': user_form,
		 'registered': registered})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse('Your Essential Oils account is disabled.')
		else:
			print('Invalid login details: {0}, {1}'.format(username, password))
			return HttpResponse('Invalid login details supplied.<br/>Details given: <br/>'+
				'<p style="text-indent: 25px;">Username: '+username+'</p>'+
				'<p style="text-indent: 25px;">Password: '+password+'</p>')
	else:
		return render(request, 'catalog/login.html', {})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))