from django.shortcuts import render
from django.views import generic
# Create your views here.
from .models import Course, UsersStats
from .models import Card
def index(request):
    num_cards = Card.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_cards':num_cards},
    )

class CourseListView(generic.ListView):
    model = Course

class CourseDetailView(generic.DetailView):
    model = Course

class CardListView(generic.ListView):
    model = Card

class CardDetailView(generic.DetailView):
    model = Card
