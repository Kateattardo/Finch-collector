from django.db import models
from django.urls import reverse

# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

#Toy Model
# Finchs >------<Toys
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.color} {self.name}'

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)


    def __str__(self):
        return self.name
    
    # this is used for redirects from class based views
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)


# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
  

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    # this is used for redirects from class based views
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

    


class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
	choices=MEALS,
	default=MEALS[0][0]
  )
#create finch Fk refernce
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
  

def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

class Meta:
    ordering = ['-date']
  