#!/usr/bin/env python3

from django.urls import path

from .views import homepage_view, therapist_view

urlpatterns = [
    path("", homepage_view, name="home"),
    path("<int:therapist_pk>/", therapist_view, name="therapist")
]
