from django.core.exceptions import ValidationError
import re


def validate_domainonly_email(value):
    """
    Let's validate the email passed is in the domain "yourdomain.com"
    """
    if not "yourdomain.com" in value:
        raise ValidationError(
            "Sorry, the email submitted is invalid. All emails have to be registered on this domain only.")


def validate_alpha_numeric(value):
    """
    Let's validate the email passed is in the domain "yourdomain.com"
    """
    if not re.match(r'^[0-9a-zA-Z ]*$', value):
        raise ValidationError(
            "Sorry, Input should contain only [a-z][A-Z][0-9] (alphanumeric characters) only.")
