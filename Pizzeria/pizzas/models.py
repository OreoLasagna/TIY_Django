from django.db import models

# Create your models here.
class Pizza(models.Model):
    """A pizza model that can hold names of pizzas"""
    name = models.CharField(max_length = 50)

    def __str__(self):
        """Return a string representation of the model"""
        return self.name


class Topping(models.Model):
    """A topping model that relates to pizzas"""
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    #Keeping name a CharField since toppings shouldn't be that long in text size

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        """Return a string representation of the model"""
        return self.name