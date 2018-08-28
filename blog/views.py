from django.shortcuts import render

def profile(request):
    return render(request, 'blog/profile.html')

def resume(request):
    return render(request, 'blog/resume.html', {})

def portfolio(request):
    return render(request, 'blog/portfolio.html', {})

def calculator(request):
    return render(request, 'blog/calculator_site.html', {})

def game(request):
    return render(request, 'blog/game_site.html', {})

def image_viewer(request):
    return render(request, 'blog/image_viewer_site.html', {})


def contact(request):
    return render(request, 'blog/contact.html', {})

def design(request):
    return render(request, 'blog/design.html', {})





