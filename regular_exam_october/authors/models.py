from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.db import models


def validate_letters_only(value):
    if not value.isalpha():
        raise ValidationError("Your name must contain letters only!")


def validate_passcode(value):
    if not value.isdigit() or len(value) != 6:
        raise ValidationError("Your passcode must be exactly 6 digits!")


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(40),
            validate_letters_only
        ],
        help_text="Your first name must contain letters only."
    )
    last_name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(50),
            validate_letters_only
        ],
        help_text="Your last name must contain letters only."
    )
    passcode = models.CharField(
        max_length=6,
        blank=False,
        null=False,
        validators=[validate_passcode],
        help_text="Your passcode must be a combination of 6 digits.",
    )
    pets_number = models.PositiveSmallIntegerField(
        blank=False,
        null=False,
    )
    info = models.TextField(
        blank=True,
        null=True,
    )
    image_url = models.URLField(
        blank=True,
        null=True
    )
