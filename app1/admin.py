from django.contrib import admin
# from django.contrib import ModelAdmin
from .models import Doubts


class DoubtsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "desc")


admin.site.register(Doubts, DoubtsAdmin)
# Register your models here.
