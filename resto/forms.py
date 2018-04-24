from django import forms

from .models import Resto
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticMapWidget, GoogleStaticOverlayMapWidget

class RestoCreateForm(forms.ModelForm):

	class Meta:
		model=Resto
		fields = ("name","address")
		widgets = {
		'address' : GooglePointFieldWidget,
		}

class RestoDetailForm(forms.ModelForm):
	
	class Meta:
		model = Resto
		fields= ('name','address')
		widgets = {
		'address': GooglePointFieldWidget(zoom=12,size = "250x250")
		}