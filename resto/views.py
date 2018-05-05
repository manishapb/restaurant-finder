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

	# def form_valid(self,form):
	# 	print(self.request)
	# 	item = form.save(commit=False)

	# 	resto = Resto.objects.get(pk=self.request.POST.get('resto'))
	# 	item.resto = resto
	# 	return super(AddDishView,self).form_valid(form)


def search(request):
	if request.method=='GET':
		lat = float(request.GET.get('user_lat'))
		lng = float(request.GET.get('user_long'))
		radius = float(request.GET.get('user_radius'))

		point = Point(lng,lat)
		restos = Resto.objects.filter(address__distance_lte=(point, D(m=radius)))

		if request.GET.get('user_veg_only'):
			dishes = Dish.objects.filter(resto__in=restos,veg=True)
		else:
			dishes = Dish.objects.filter(resto__in=restos)

		return render(request,'resto/result.html',{'dishes':dishes})

		
class DishDetailView(DetailView):
	template_name = 'dish/detail.html'
	model = Dish

	def get_object(self,**kwargs):
		context = get_object_or_404(Dish,pk=self.kwargs.get('dish_id',None))
		return context

def home_page(request):
	return render(request,'home.html', {})
