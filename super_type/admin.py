from django.contrib import admin

from supers.models import Supers
from .models import Super_Type


admin.site.register(Supers)
admin.site.register(Super_Type)
