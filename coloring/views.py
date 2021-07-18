from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')

def pencil_brush(request):
    return render(request, 'coloring/pencil_brush.html')

def flat_brush(request):
    return render(request, 'coloring/flat_brush.html')

def bucket(request):
    return render(request, 'coloring/bucket.html')

def drawing_screen(request):
    return render(request, 'coloring/drawing_screen.html')

def home(request):
    return render(request, 'coloring/home.html')