from django.shortcuts import render, redirect
# we need to import our class based views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.import ListView
from django.views.generic.detail import DetailView

from .models import Finch, Toy
from .forms import FeedingForm

finchs = [
  {'breed': 'American Goldfinch', 'description': 'vibrant yellow with some balck markings'},
  {'breed': 'Housefinch', 'description': 'red and lightbrown'},
  {'breed': 'Strawberry finch', 'description': 'vibrant red with white and balck markings'},
]

# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finchs_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', { 'finches': finches})

def finchs_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    id_list = finch.toys.all().values_list('id')
    toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)
    return render(request, 'finchs/detail.html', { 'finch': finch, 'feeding_form': feeding_form, 'toys': toys_finch_doesnt_have })
    return redirect('detail', finch_id=finch_id)

def add_feeding(request, finch_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
  model = Finch
  # fields = '__all__'
  fields = ['name', 'breed', 'description', 'age']
  success_url = '/finchs/{finch_id}'

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['breed', 'description','age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finchs'

#Views for Toys

# # ToyList
class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'

# # ToyDetail
class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/detail.html'

# # ToyCreate
class ToyCreate(CreateView):
    model = Toy
    fields = ['name', 'color']

    def form_valid(self, form):
        return super().form_valid(form)

# ToyUpdate
class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

# ToyDelete
class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

# adds toy to finch
def assoc_toy(request, finch_id, toy_id):
    # to make the association, we target the cat and pass the toy id
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    return redirect('detail', finch_id=finch_id)
# removes toy from finch
def unassoc_toy(request, finch_id, toy_id):
    # to make the association, we target the finch and pass the toy id
    Finch.objects.get(id=finch_id).toys.remove(toy_id)
    