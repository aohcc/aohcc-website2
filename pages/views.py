from django.shortcuts import render

from .models import Therapist


def home_page_view(request):
    therapists = Therapist.objects.filter(active=True)
    return render(request, "home.html", {"therapists": therapists})
