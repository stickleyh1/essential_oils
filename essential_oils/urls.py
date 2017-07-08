from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, url
from django.conf.urls import include
from django.contrib import admin
from django.views.generic import RedirectView
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
	def get_success_url(self, user):
		return '/catalog/'

urlpatterns = [
	url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),
    url(r'^admin/', admin.site.urls),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)