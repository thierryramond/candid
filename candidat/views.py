from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView, FormView
from candidat.models import Candidature
from candidat.forms import * 


#-----------------------------------------------------------------------------
# index

def home(request):
	return render(request,'candidat/accueil.html',{'datetime': timezone.now()})


#-----------------------------------------------------------------------------
#

class CandidatureListView(ListView):
	model = Candidature
	template_name = 'candidat/candidature_list.html'
	ordering = 'nom'


class CandidatureCreateView(FormView):
	template_name = 'candidat/candidature_create.html'
	form_class  = CandidatureForm
	success_url = reverse_lazy('candidats')

	def form_valid(self,form):
		the_candidature = Candidature(
			nom = form.cleaned_data['nom'],
			prenom = form.cleaned_data['prénom'],
			année = form.cleaned_data['année'],
			)
		the_candidature.save()

		return HttpResponseRedirect(self.get_success_url())

	


