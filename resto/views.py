from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,ListView,DetailView
from .forms import RestoCreateForm,RestoDetailForm
from django.urls import reverse_lazy
from .models import Resto

class RestoCreateView(CreateView):
	template_name = "resto/form.html"
	form_class = RestoCreateForm
	success_url = reverse_lazy("resto:list")

	def form_valid(self, form):
		form.save()
		return super(RestoCreateView, self).form_valid(form)


class ListRestoView(ListView):
	template_name="resto/list.html"
	queryset = Resto.objects.all()
	context_object_name = 'resto'

class DetailRestoView_Od(DetailView):
	model = Resto
	template_name = 'resto/detail.html'

	def get_object(self,**kwargs):
		context = get_object_or_404(Resto,pk=self.kwargs.get('pk',None))
		print(context.name)
		return context

class DetailRestoView(DetailView):
	form_class = RestoDetailForm
	model = Resto
	template_name = 'resto/detail.html'