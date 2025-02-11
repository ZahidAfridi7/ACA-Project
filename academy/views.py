from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def players(request):
    return render(request, 'all_players.html')

def register(request):
    return render(request , 'register.html')

def about(request):
    return render(request , 'about.html')

def feedback(request):
    return render(request, 'feedback.html')