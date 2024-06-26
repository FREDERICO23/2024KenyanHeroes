from django.shortcuts import render, redirect, get_object_or_404
from .models import Hero
from .forms import HeroForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def hero_create(request):
    if request.method == 'POST':
        form = HeroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hero_list')
    else:
        form = HeroForm()
    return render(request, 'hero_form.html', {'form': form})

def hero_list(request):
    heroes = Hero.objects.all()
    return render(request, 'index.html', {'heroes': heroes})

def hero_detail(request, pk):
    hero = get_object_or_404(Hero, pk=pk)
    return render(request, 'hero_detail.html', {'hero': hero})

def hero_update(request, pk):
    hero = get_object_or_404(Hero, pk=pk)
    if request.method == 'POST':
        form = HeroForm(request.POST, request.FILES, instance=hero)
        if form.is_valid():
            form.save()
            return redirect('hero_list')
    else:
        form = HeroForm(instance=hero)
    return render(request, 'hero_form.html', {'form': form})

def hero_delete(request, pk):
    hero = get_object_or_404(Hero, pk=pk)
    if request.method == 'POST':
        hero.delete()
        return redirect('hero_list')
    return render(request, 'hero_confirm_delete.html', {'hero': hero})