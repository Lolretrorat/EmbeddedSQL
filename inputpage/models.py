from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import uuid

def validate_gender(value):
    if value not in ['M', 'F', 'N']:
        raise ValidationError(
            _('Gender must be one of the following: M, F, N.'),
            params={'value': value},
        )

class Address(models.Model):
    address_token = models.AutoField(primary_key=True)
    street_number = models.CharField(max_length=10)
    street_name = models.CharField(max_length=50)
    suburb = models.CharField(max_length=50)
    postcode = models.CharField(max_length=4)
    state = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.street_number} {self.street_name}, {self.suburb}, {self.state}, {self.postcode}"

    def save(self, *args, **kwargs):
        if not self.address_id:
            self.address_id = uuid.uuid4().hex
        super().save(*args, **kwargs)

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True, unique=True, editable=False)
    salutation = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, validators=[validate_gender])
    contact_number = models.CharField(max_length=15)
    medicare_number = models.CharField(max_length=15)
    address_token = models.ForeignKey(Address, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return f"{self.salutation} {self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.patient_id:
            self.patient_id = uuid.uuid4().hex
        super().save(*args, **kwargs)

class Practitioner(models.Model):
    practitioner_id = models.AutoField(primary_key=True, unique=True, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    primary_location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.job_title}"

    def save(self, *args, **kwargs):
        if not self.practitioner_id:
            self.practitioner_id = uuid.uuid4().hex
        super().save(*args, **kwargs)

class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=50)
    service_description = models.CharField(max_length=100)
    service_medicare_item_number = models.CharField(max_length=15)
    service_type = models.CharField(max_length=50)

    def __str__(self):
        return self.service_name

class Consultation(models.Model):
    consultation_id = models.AutoField(primary_key=True, unique=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    practitioner_id = models.ForeignKey(Practitioner, on_delete=models.CASCADE)
    consultation_time = models.DateField()
    consultation_type = models.CharField(max_length=50)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return f"Consultation for {self.patient_id} with {self.practitioner_id} at {self.consultation_time}"

    def save(self, *args, **kwargs):
        if not self.consultation_id:
            self.consultation_id = uuid.uuid4().hex
        super().save(*args, **kwargs)
