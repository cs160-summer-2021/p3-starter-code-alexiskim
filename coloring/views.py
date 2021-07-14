from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')

def varied_width_brush(request):
    return render(request, 'coloring/varied_width_brush.html')

def flat_brush(request):
    return render(request, 'coloring/flat_brush.html')