from django.contrib import admin
from candidat.models import Candidature,Etudiant
# Register your models here.

class CandidatureAdmin(admin.ModelAdmin):
	list_display   = ('nom', 'prénom', 'année')
	ordering       = ('nom', )

class EtudiantAdmin(admin.ModelAdmin):
	list_display   = ('nom', 'prenom',)
	ordering       = ('nom', )

admin.site.register(Candidature,CandidatureAdmin)
admin.site.register(Etudiant,EtudiantAdmin)
