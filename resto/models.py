from django.db import models as dmodels
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models import Manager as GeoManager
from django.core.validators import MaxValueValidator, MinValueValidator


class WorldBorder(models.Model):
	fips = models.CharField(max_length=2)
	iso2 = models.CharField(max_length=2)
	iso3 = models.CharField(max_length=3)
	un = models.IntegerField()
	name = models.CharField(max_length=50)
	area = models.IntegerField()
	pop2005 = models.IntegerField()
	region = models.IntegerField()
	subregion = models.IntegerField()
	lon = models.FloatField()
	lat = models.FloatField()
	geom = models.MultiPolygonField(srid=4326)


class Resto(models.Model):
	name=models.CharField(max_length=200)
	address = models.PointField()

	def __unicode__(self):
		return self.name


class Dish(dmodels.Model):
	name = dmodels.CharField(max_length=200)
	description = dmodels.CharField(max_length=500)
	cost = dmodels.FloatField()
	resto = dmodels.ForeignKey(Resto,on_delete=dmodels.CASCADE)
	veg = dmodels.BooleanField(default=True)
	rating = dmodels.FloatField(null=True,blank=True,default=None,
		validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)
	image = dmodels.ImageField(upload_to="resto/", null=True,blank=True,default=None)

	def __unicode__(self):
		return self.name