from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .models import Therapist, Faq, InsurancePageText, AboutUs


def homepage_view(request):
    therapists = Therapist.objects.filter(active=True).order_by("last_name")
    therapist_insurances = {
        therapist.first_name: therapist.insurances.all() for therapist in therapists
    }
    about_us = AboutUs.objects.get(pk=1)

    context = {
        "therapists": therapists,
        "therapist_insurances": therapist_insurances,
        "about_us": about_us,
    }

    return render(request, "home.html", context)


def therapist_view(request, therapist_pk):
    therapist = get_object_or_404(Therapist, pk=therapist_pk)
    context = {"therapist": therapist}

    return render(request, "therapist.html", context)


def faq_view(request):
    faqs = Faq.objects.all().order_by("id")
    context = {"faqs": faqs}

    return render(request, "faq.html", context)


def insurance_view(request):
    insurance_sections = InsurancePageText.objects.all()
    context = {"insurance_sections": insurance_sections}

    return render(request, "insurance.html", context)
