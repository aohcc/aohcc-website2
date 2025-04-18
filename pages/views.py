from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .models import Therapist, Faq, InsurancePageText, AboutUs

from .forms import ContactForm

def success_view(request):
    therapists = Therapist.objects.filter(active=True).order_by("last_name")
    about_us = AboutUs.objects.get(pk=1)

    context = {"therapists": therapists, "about_us": about_us}

    return render(request, "success.html", context)

def homepage_view(request):
    therapists = Therapist.objects.filter(active=True).order_by("last_name")
    therapists_info_list = []
    for therapist in therapists:
        insurances = []
        populations = []
        for insurance in therapist.insurances.all():
            insurances.append(insurance.name)
        for population in therapist.populations.all():
            populations.append(population.group)
        therapists_info_list.append(
            {
                "id": therapist.pk,
                "first_name": therapist.first_name,
                "last_name": therapist.last_name,
                "license_type": therapist.license_type,
                "accepting_new_clients": therapist.accepting_clients,
                "insurances": ", ".join(insurances),
                "populations": ", ".join(populations),
                "picture_filename": therapist.picture_filename
             }
        )
    about_us = AboutUs.objects.get(pk=1)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            message = form.cleaned_data["message"]

            recipients = ["clientcare@aohcc.com"]

            send_mail(
                "AOHCC Inquiry from Website",
                f"{name}\n{phone}\n{email}\n{message}",
                None,
                recipients,
            )

            return HttpResponseRedirect("success")

    else:
        form = ContactForm()

    context = {
        "therapists_info_list": therapists_info_list,
        "about_us": about_us,
        "form": form,
    }

    return render(request, "home.html", context)


def therapist_view(request, therapist_pk):
    therapist = get_object_or_404(Therapist, pk=therapist_pk)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            message = form.cleaned_data["message"]

            recipients = ["clientcare@aohcc.com"]

            send_mail(
                "AOHCC Inquiry from Website",
                f"{name}\n{phone}\n{email}\n{message}",
                email,
                recipients,
            )

            return HttpResponseRedirect("/thanks/")

    else:
        form = ContactForm()

    context = {"therapist": therapist, "form": form}

    return render(request, "therapist.html", context)


def faq_view(request):
    faqs = Faq.objects.all().order_by("id")
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            message = form.cleaned_data["message"]
            recipients = ["clientcare@aohcc.com"]

            send_mail(
                "AOHCC Inquiry from Website",
                f"{name}\n{phone}\n{email}\n{message}",
                email,
                recipients,
            )

            return HttpResponseRedirect("/thanks/")

    else:
        form = ContactForm()

    context = {"faqs": faqs, "form": form}

    return render(request, "faq.html", context)


def insurance_view(request):
    insurance_sections = InsurancePageText.objects.all()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            message = form.cleaned_data["message"]

            recipients = ["clientcare@aohcc.com"]

            send_mail(
                "AOHCC Inquiry from Website",
                f"{name}\n{phone}\n{email}\n{message}",
                email,
                recipients,
            )

            return HttpResponseRedirect("/thanks/")

    else:
        form = ContactForm()

    context = {"insurance_sections": insurance_sections, "form": form}

    return render(request, "insurance.html", context)


def contact_form_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            message = form.cleaned_data["message"]

            recipients = ["clientcare@aohcc.com"]

            send_mail(
                "AOHCC Inquiry from Website",
                f"{name}\n{phone}\n{email}\n{message}",
                email,
                recipients,
            )

            return HttpResponseRedirect("/thanks/")

    else:
        form = ContactForm()

    return render(request, "base.html", {"form": form})
