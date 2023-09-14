from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
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
    return render(request, 'finchs/detail.html', {
    'finch': finch, 'feeding_form': feeding_form
  })
  
    return render(request, 'finches/detail.html', { 'finch': finch})
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
  fields = '__all__'
  success_url = '/finchs/{finch_id}'

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['breed', 'description',]

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finchs'

# # ToyList
# class ToyList(ListView):
#     model = Toy
#     template_name = 'toys/index.html'

# # ToyDetail
# class ToyDetail(DetailView):
#     model = Toy
#     template_name = 'toys/detail.html'

# # ToyCreate
# class ToyCreate(CreateView):
#     model = Toy
#     fields = ['name', 'color']

#     def form_valid(self, form):
#         return super().form_valid(form)