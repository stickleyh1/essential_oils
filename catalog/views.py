from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.db.models import Q

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

from django.core.mail import send_mail

import uuid
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
			objs = Product.objects.filter(Q(name__icontains=query) | Q(ailments__name__icontains=query)).distinct().order_by('isBlend', 'name')
			for p in objs:
				results.append(p)
			return render(request, 'catalog/search_results.html', {"results": results,})

	return render(request, 'catalog/search.html')

@login_required
def product_added(request):
	if 'current' in request.session:
		if 'cart' in request.session:
			cart = request.session['cart']
			cart.append(request.session['current'])
			request.session['cart'] = cart
		else:
			request.session['cart'] = [request.session['current']]
		request.session.modified = True

	return HttpResponseRedirect(reverse('product'))

@login_required
def cart(request):
	products = []
	if 'cart' in request.session:
		ids = []
		for idStr in request.session['cart']:
			ids.append(uuid.UUID(idStr[0]).hex)
		objs = Product.objects.filter(pk__in=ids)
		total = 0
		for p in objs:
			total += p.price
			products.append(p)
		return render(request, 'catalog/cart.html', {"cart": products, "total": total})
	return render(request, 'catalog/cart.html')

@login_required
def checkout(request):
	if request.user.is_authenticated():
		#Saving order
		total = 0
		ids = []
		for idStr in request.session['cart']:
			ids.append(uuid.UUID(idStr[0]).hex)

		order = Order.objects.create(id=uuid.uuid4())
		objs = Product.objects.filter(pk__in=ids)
		for p in objs:
			total = total + p.price
		request.session['cart'] = []
		request.session.modified = True
		order.total=total
		order.buyer=request.user
		order.products=objs
		order.save()

		admins = User.objects.filter(is_staff=True)

		# HTML message for email
		htmlmessage = '<p style="margin-left:25px">'+str(order)+'</p><ul>'
		for product in objs:
			htmlmessage += '<li>' +str(product)+ '</li>'
		htmlmessage += '</ul>'

		# Plain text message for email
		message = str(order)+'\n'
		for product in objs:
			message += '>>>' +str(product)+ '\n'

		email_list = []
		for admin in admins:
			email_list.append(admin.email)
		send_mail('New Order from '+str(order.buyer.username), message, 'stickleyh1@student.lasalle.edu', email_list, html_message=htmlmessage)

	return HttpResponseRedirect(reverse('index'))

@login_required
def clear_cart(request):
	if request.user.is_authenticated():
		request.session['cart'] = []
		request.session.modified = True
	return HttpResponseRedirect(reverse('index'))

def UserDetailsView(request):
	if request.user.is_authenticated():
		orders = Order.objects.filter(buyer=request.user)
		return render(request, 'catalog/user_details.html', {'orders': orders})
	else:
		return HttpResponseRedirect(reverse('index'))

class ProductListView(generic.ListView):
    model = Product

class ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        self.request.session['current'] = [str(self.object.pk)]
        self.request.session.modified = True
        return context

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