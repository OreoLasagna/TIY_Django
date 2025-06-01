from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for this Meal Planning"""
    return render(request, 'meal_planning/index.html')