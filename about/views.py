from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import About

# Create your views here.

def about(request):

    about = About.objects.all().order_by('updated_on').first()

    context = {
        "about": about,
    }

    return render(
        request, "about/about.html", context,
    )

