from importlib import import_module
from django.contrib import admin

# Register your models here.
from .models import Score, Customer, Score_hist
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin









admin.site.register(Customer,ImportExportModelAdmin)
admin.site.register(Score,ImportExportModelAdmin)
admin.site.register(Score_hist,ImportExportModelAdmin)



















