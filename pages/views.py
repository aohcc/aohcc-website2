from django.shortcuts import render, get_object_or_404

from .models import Therapist, Faq, InsurancePageText


def homepage_view(request):
    therapists = Therapist.objects.filter(active=True).order_by("last_name")
    return render(request, "home.html", {"therapists": therapists})


def therapist_view(request, therapist_pk):
    therapist = get_object_or_404(Therapist, pk=therapist_pk)
    return render(request, "therapist.html", {"therapist": therapist})


def faq_view(request):
    faqs = Faq.objects.all().order_by("id")
    return render(request, "faq.html", {"faqs": faqs})

def insurance_view(request):
    insurance_sections = InsurancePageText.objects.all()
    return render(request, "insurance.html", {"insurance_sections": insurance_sections})
