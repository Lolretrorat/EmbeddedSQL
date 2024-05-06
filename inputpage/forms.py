from django import forms
from .models import Address, Patient, Practitioner, Service, Consultation

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street_number', 'street_name', 'suburb', 'postcode', 'state']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['salutation', 'first_name', 'last_name', 'date_of_birth', 'gender', 'contact_number', 'medicare_number', 'address_token']

class PractitionerForm(forms.ModelForm):
    class Meta:
        model = Practitioner
        fields = ['first_name', 'last_name', 'job_title', 'contact_number', 'primary_location']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_name', 'service_description', 'service_medicare_item_number', 'service_type']

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['patient_id', 'practitioner_id', 'consultation_time', 'consultation_type', 'service_id']
