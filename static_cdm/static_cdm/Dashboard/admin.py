from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import *
from .models import Categorie,EditionLivre
#from .models import Categorie,EditionLivre
# Register your models here.
#AdminSite.site_header = "ComptaRosius Administration"
admin.site.register(Categorie)
admin.site.register(EditionLivre)
admin.site.register(TypeeDition)
admin.site.register(Thematiques)
admin.site.register(EditionContact)