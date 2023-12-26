from django.contrib import admin
from .models import State, Town, Person


admin.site.register(State)
admin.site.register(Town)
admin.site.register(Person)