#!/usr/bin/env python3

from django.urls import path

from .views import homepage_view, therapist_view, faq_view, insurance_view, success_view

urlpatterns = [
    path("", homepage_view, name="home"),
    path("<int:therapist_pk>/", therapist_view, name="therapist"),
    path("faq", faq_view, name="faq"),
    path("insurance", insurance_view, name="insurance"),
    path("success", success_view, name="success")
]
