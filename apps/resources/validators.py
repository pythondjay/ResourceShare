from django.core.exceptions import ValidationError


def check_rating_range(value):
    if value < 0 or value > 5:
        raise ValidationError(f"{value} is not valid. It must be between 0 and 5")
