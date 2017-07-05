from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext
import datetime as dt

from django.db.models import Q
from django.contrib.auth.models import User
from catalog.models import Order, Product, Ailment

def index(request):
	context_dict={}
	return render(request, 'catalog/index.html')

# class UserListView(generic.ListView):
#     model = User