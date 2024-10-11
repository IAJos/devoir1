from django.db import models
from django.core.validators import MinValueValidator


class School(models.Model):
    class Sector(models.TextChoices):
        COMMERCE = 'Commerce'
        DROIT = 'Droit'
        INFORMATIQUE = 'Informatique'

    name = models.fields.CharField(max_length=30)
    email = models.fields.EmailField(max_length=50)
    # password = models.fields.DecimalField()
    site = models.fields.URLField()
    creation_date = models.fields.DateField()
    start_time = models.fields.TimeField()
    student_number = models.fields.IntegerField(validators=[MinValueValidator(1)])
    tuition_fees = models.fields.FloatField(validators=[MinValueValidator(10000.0)])
    sector = models.fields.TextField(choices=Sector.choices)
    is_eed = models.fields.BooleanField(default=True)
# Create your models here.
