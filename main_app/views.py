from django.shortcuts import render

finchs = [
  {'breed': 'goldfinch', 'description': 'gold with some balck'},
  {'breed': 'housefinch', 'description': 'red and lightbrown'},
]

# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finch_index(request):
  return render(request, 'finches/index.html', { 'finches': finches})
