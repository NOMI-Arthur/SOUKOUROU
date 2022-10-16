from django.contrib import admin
from .models import Travailleur, Enseignant
#from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Travailleur)
admin.site.register(Enseignant)