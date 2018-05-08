from django.contrib import admin
from resto.models import Resto,Dish
from mapwidgets.widgets import GooglePointFieldWidget
from django.contrib.gis.db import models
from django import forms
# Register your models here.

CUSTOM_MAP_SETTINGS = {
    "GooglePointFieldWidget": (
        ("zoom", 15),
        ("mapCenterLocation", [28.6562, 77.2410]),
    ),
}

class RestoAdminForm(forms.ModelForm):
    class Meta:
        model = Resto
        fields = ("name", "address")
        widgets = {
            'address': GooglePointFieldWidget(settings=CUSTOM_MAP_SETTINGS),
            }

class RestoAdmin(admin.ModelAdmin):
    list_display = ("name", "address")

    def get_form(self, request, obj=None, **kwargs):
        self.form = RestoAdminForm
        return super(RestoAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(Resto, RestoAdmin)
admin.site.register(Dish)
