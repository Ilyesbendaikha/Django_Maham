from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(client)
admin.site.register(voyage)
admin.site.register(Place)
admin.site.register(order)

