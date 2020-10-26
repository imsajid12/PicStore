from django.shortcuts import render
from mainapp.models import *

def show_about_page(request):
    return render(request, "about.html")


def show_index_page(request):
    categories = Category.objects.all()
    images = Image.objects.all()
    context = {'images':images, 'categories': categories}
    return render(request, "index.html", context)

def show_images_as_per_category(request, cid):
    categories = Category.objects.all()

    category = Category.objects.get(pk=cid)

    images = Image.objects.filter(cat=category)
    context = {'images':images, 'categories': categories, 'category' : category}
    return render(request, "index.html", context)