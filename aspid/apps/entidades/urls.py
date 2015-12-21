from django.conf.urls import url
from .views import EmpresaSingleTableView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required

#from apps.decorators import custom_permission_required

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='base/divided.html'), name='entidades'),
    url(r'^empresa/$', (EmpresaSingleTableView.as_view()), name ='lista_de_empresas'),
]