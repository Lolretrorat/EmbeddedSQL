from django.contrib import admin
from .models import Address, Patient, Practitioner, Service, Consultation

admin.site.register(Address)
admin.site.register(Patient)
admin.site.register(Practitioner)
admin.site.register(Service)
admin.site.register(Consultation)

