from django import forms

from .models import Resto,Dish
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticMapWidget, GoogleStaticOverlayMapWidget

class RestoCreateForm(forms.ModelForm):

	class Meta:
		model=Resto
		fields = ("name","address")
		widgets = {
		'address' : GooglePointFieldWidget,
		}

	def is_valid(self):
		return True

class RestoUpdateForm(forms.ModelForm):
	
	class Meta:
		model = Resto
		fields= ('name','address')
		widgets = {
		'address': GooglePointFieldWidget,
		}

class CreateDishForm(forms.ModelForm):

	class Meta:
		model = Dish
		fields = ('name','description','cost','resto')
