from django.contrib import admin
from candidat.models import Candidature
# Register your models here.

class CandidatureAdmin(admin.ModelAdmin):
    list_display   = ('nom', 'prénom', 'année')
    ordering       = ('nom', )

admin.site.register(Candidature,CandidatureAdmin)
