from django.contrib import admin

from .models import Therapist, Certification, Insurance, Population

admin.site.register(Therapist)
admin.site.register(Certification)
admin.site.register(Insurance)
admin.site.register(Population)
