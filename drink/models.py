from django.db import models

class MainMenu(models.Model):
	name = models.CharField(max_length = 45)

	class Meta:
		db_table = 'menu'

class Category(models.Model):
	menu       = models.ForeignKey('MainMenu', on_delete = models.CASCADE)
	name       = models.CharField(max_length = 45)
	decaffeine = models.ForeignKey('DeCaffeineShot', on_delete = models.SET_NULL, null = True)

	class Meta:
		db_table = 'categories'

class Nutrition(models.Model):
	kcal     = models.DecimalField(max_digits = 10, decimal_places = 2)
	sodium   = models.DecimalField(max_digits = 10, decimal_places = 2)
	sat_fat  = models.DecimalField(max_digits = 10, decimal_places = 2)
	sugar    = models.DecimalField(max_digits = 10, decimal_places = 2)
	protein  = models.DecimalField(max_digits = 10, decimal_places = 2)
	caffeine = models.DecimalField(max_digits = 10, decimal_places = 2)
	
	class Meta:
		db_table = 'nutritions'

class Drink(models.Model):
	menu          = models.ForeignKey('MainMenu', on_delete = models.SET_NULL, null = True)
	category      = models.ForeignKey('Category', on_delete = models.SET_NULL, null = True)
	nutrition     = models.OneToOneField('Nutrition', on_delete = models.SET_NULL, null = True)
	allergy_drink = models.ManyToManyField('Allergy', through = 'DrinkAllergy') #복습
	name          = models.CharField(max_length = 100)
	en_name       = models.CharField(max_length = 200) 
	is_mydrink    = models.BooleanField(default = False)

	class Meta:
		db_table = 'drinks'

class Allergy(models.Model):
	name = models.CharField(max_length = 45)

	class Meta:
		db_table = 'allergies'

class DrinkAllergy(models.Model):
	drink   = models.ForeignKey('Drink', on_delete = models.SET_NULL , null = True)
	allergy = models.ForeignKey('Allergy', on_delete = models.SET_NULL, null = True)
	
	class Meta:
		db_table = 'drinks_allergies'

class DrinkImage(models.Model):
	drink = models.ForeignKey('Drink', on_delete = models.SET_NULL, null = True)
	image = models.URLField(max_length = 2000)

	class Meta:
		db_table = 'images'

class Description(models.Model):
	description_top    = models.CharField(max_length = 1000)
	description_bottom = models.CharField(max_length = 1000)
	drink              = models.ForeignKey('Drink', on_delete = models.SET_NULL, null = True)

	class Meta:
		db_table = 'descriptions'

class Size(models.Model):
	name         = models.CharField(max_length = 45)
	ml           = models.IntegerField(default = 0)
	oz           = models.IntegerField(default = 0)
	nutrition    = models.ForeignKey(Nutrition, on_delete = models.SET_NULL, null = True)

	class Meta:
		db_table = 'sizes'

class DeCaffeineShot(models.Model):
	decaffeine_espresso = models.BooleanField(default = False)

	class Meta:
		db_table = 'decaffeine_shots'
