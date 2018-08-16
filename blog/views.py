from django.shortcuts import render

def profile(request):
    return render(request, 'blog/profile.html', {})

def game(request):
    return render(request, 'blog/game.html', {})

def calculator(request):
    return render(request, 'blog/calculator.html', {})

def image_viewer(request):
    return render(request, 'blog/image_viewer.html', {})


def contact(request):
    return render(request, 'blog/contact.html', {})





