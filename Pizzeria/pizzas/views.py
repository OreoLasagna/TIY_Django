from django.shortcuts import render

from .models import Pizza

def index(request):
    """The home page for Pizzeria."""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Page showing all pizzas that are available."""
    pizzas = Pizza.objects.all()
    #Okay so for pizzas we just grab... everything. We want every bit of information we can get about pizzas
    #Which includes: name, date_added
    context = {'pizzas': pizzas}
    #We pass the pizza dictionary to the pizzas.html file
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    """Page showing information about an individual pizza."""
    pizza = Pizza.objects.get(id=pizza_id)
    #We are grabbing the very specific pizza.
    #This id is passed in by the urls.py file
    #Then when the pizzas.html file is run through those individual IDs are found and added to URLs
    toppings = pizza.topping_set.all()
    #This is some Python shenanigans not taught in the book
    #In the book they used entry_set when there is a one to one relationship.
    #Here we have to use _set which I don't fully understand why to be honest
    #https://stackoverflow.com/questions/54714887/object-has-no-attribute-entry-set-error
    #foo_set
    #I have to use the Topping class in lower case to grab this
    #Reference back to Page 387

    #But here you can have multiple toppings assigned to one pizza!

    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)