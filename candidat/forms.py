from django import forms
from .models import *

class anneeForm(forms.ModelForm):
	class Meta:
		model = Candidature
		fields = '__all__'

class CandidatureForm(forms.ModelForm):
	class Meta:
		model = Candidature
		exclude = ()