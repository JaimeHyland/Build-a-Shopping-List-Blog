from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.

def about(request):
    if request.method == "POST":
        print("The site has received a POST request")
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request submitted'
            )

    about = About.objects.all().order_by('updated_on').first()

    collaborate_form = CollaborateForm()

    context = {
        "about": about,
        "collaborate_form": collaborate_form,
    }

    return render(
        request, "about/about.html", context,
    )


