from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Stroke(models.Model):
    class GenderChoices(models.IntegerChoices):
        FEMALE = 0, _('Female')
        MALE = 1, _('Male')
        OTHERS = 2, _('Others')

    class SmokingChoices(models.IntegerChoices):
        FORMER = 0, _('Formerly Smoked')
        NEVER = 1, _('Never Smoked')
        SMOKES = 2, _('Smokes')

    class BoolChoices(models.IntegerChoices):
        FALSE = 0, _('No')
        TRUE = 1, _('Yes')

    gender = models.IntegerField(choices=GenderChoices.choices)
    age = models.FloatField(validators=[MinValueValidator(0.1)])
    hypertension = models.IntegerField(choices=BoolChoices.choices, default=BoolChoices.FALSE)
    heart_disease = models.IntegerField(choices=BoolChoices.choices, default=BoolChoices.FALSE)
    avg_glucose_level = models.FloatField(validators=[MinValueValidator(0.1)])
    bmi = models.FloatField(validators=[MinValueValidator(0.1)])
    smoking_status = models.IntegerField(choices=SmokingChoices.choices)