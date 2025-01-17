from django.shortcuts import render, get_object_or_404

from .models import Therapist


def homepage_view(request):
    therapists = Therapist.objects.filter(active=True).order_by("last_name")
    return render(request, "home.html", {"therapists": therapists})

def therapist_view(request, therapist_pk):
    therapist = get_object_or_404(Therapist, pk=therapist_pk)
    return render(request, "therapist.html", {"therapist": therapist})
