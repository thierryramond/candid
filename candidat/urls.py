from django.conf.urls import include, url
from django.contrib import admin
from .models import *
from candidat import views
from candidat.views import CandidatureListView


urlpatterns = [
	url(r'^$', 'candidat.views.home', name= 'index'),
	url(r'^accueil/', 'candidat.views.home', name= 'index'),
	url(r'^index/', 'candidat.views.home', name= 'index'),
	url(r'^home/', 'candidat.views.home', name= 'index'),

	url(r'^candidats/', views.CandidatureListView.as_view(), name='candidats',),
	url(r'^nouveau/', views.CandidatureCreateView.as_view(), name='nouveau'),

	url(r'etudiant_list/', views.EtudiantListView.as_view(),name ='etudiant_list'),
	]

