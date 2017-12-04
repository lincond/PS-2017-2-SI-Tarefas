from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^logout/', views.logout_view),
    url(r'^login/', views.login_view),
    url(r'^register/', views.registrar),
    url(r'^projeto/novo/$', views.novo_projeto),
    url(r'^projeto/$', views.ProjetoListView.as_view()),
    url(r'^$', views.home)
]
