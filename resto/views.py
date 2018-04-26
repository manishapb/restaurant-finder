from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,ListView,DetailView,UpdateView
from .forms import RestoCreateForm, RestoUpdateForm, CreateDishForm
from django.urls import reverse_lazy
from .models import Resto,Dish
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point


class RestoCreateView(CreateView):
	template_name = "resto/form.html"
	form_class = RestoCreateForm
	success_url = reverse_lazy("resto:list")

	def form_valid(self, form):
		form.save()
		return super(RestoCreateView, self).form_valid(form)


class ListRestoView(ListView):
	template_name="resto/list.html"
	default_pnt = Point(73.856255,18.516726)
	queryset = Resto.objects.filter(address__distance_lte=(default_pnt,D(km=50)))
	context_object_name = 'resto'


class DetailRestoView(DetailView):
	model = Resto
	template_name = 'resto/detail.html'

	def get_object(self,**kwargs):
		context = get_object_or_404(Resto,pk=self.kwargs.get('pk',None))
		#dishes = Dish.objects.get(resto=context)
		return context


class AddDishView(CreateView):
	template_name="resto/add_item.html"
	form_class = CreateDishForm
	success_url = reverse_lazy("resto:list")

	def form_valid(self,form):
		print(self.request)
		item = form.save(commit=False)
		resto = Resto.objects.get(pk=self.request.POST.get('resto'))
		item.resto = resto
		#item.save()
		return super(AddDishView,self).form_valid(form)

def search(request):
	if request.method=='GET':
		print(request.GET)
		search_query= request.GET.get('dish')
		print(search_query)
		search_query = search_query.strip()
		result = Dish.objects.filter(name=search_query)
		return render(request,'resto/result.html',{'result':result})

class DishDetailView(DetailView):
	template_name = 'dish/detail.html'
	model = Dish

	def get_object(self,**kwargs):
		context = get_object_or_404(Dish,pk=self.kwargs.get('pk',None))
		return context