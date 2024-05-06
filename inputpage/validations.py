from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

def validate_gender(value):
    if value not in ['M', 'F', 'N']:
        raise ValidationError(
            _('Gender must be one of the following: M, F, N.'),
            params={'value': value},
        )

def mandatory_field_validation(instance):
    if not instance.mandatory_field:
        raise ValidationError({'mandatory_field': 'This field is required.'})

def foreign_key_validation(instance):
    if instance.foreign_key.some_field != instance.some_field:
        raise ValidationError({'foreign_key': 'The related object does not match some_field.'})

def data_type_validation(instance):
    if instance.field1 and instance.field2:
        raise ValidationError({'field1': 'Field1 and Field2 cannot both be true.'})

def required_field_validation(instance):
    if not instance.field:
        raise ValidationError('This field is required.')
