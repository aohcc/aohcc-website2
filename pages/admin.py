from django.contrib import admin

from .models import Therapist, Certification, Insurance, Population, Faq, InsurancePageText

admin.site.register(Therapist)
admin.site.register(Certification)
admin.site.register(Insurance)
admin.site.register(Population)
admin.site.register(Faq)
admin.site.register(InsurancePageText)
