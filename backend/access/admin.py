from django.contrib import admin
from .models import Role, Function, Sector, CustomUser

admin.site.register(Role)
admin.site.register(Function)
admin.site.register(Sector)
admin.site.register(CustomUser)