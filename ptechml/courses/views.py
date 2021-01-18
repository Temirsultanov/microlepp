from django.shortcuts import render

# Create your views here.
from .models import Course, Card, UsersStats

def index(request):
    num_cards = Card.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_cards':num_cards},
    )