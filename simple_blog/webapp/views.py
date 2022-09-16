from django.shortcuts import render
from simple_blog.webapp.cat import cat


def home(request):
    return render(request, 'webapp/home.html')


def cats_stats(request):
    context = {
        'name': request.POST.get('name'),
        'image': cat.change_image(),
        'age': cat.age,
        'satiety': cat.change_satiety(request.POST.get('cat_actions')),
        'happiness': cat.change_happiness(request.POST.get('cat_actions')),
        'activity': cat.set_activity(request.POST.get('cat_actions')),
    }
    return render(request, 'webapp/cats_stats.html', context)

