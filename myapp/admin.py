from django.contrib import admin

# Register your models here.

from myapp.models import Poem, Abzac
admin.site.register(Poem)
admin.site.register(Abzac)