# Generated by Django 4.2.5 on 2023-09-20 06:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stroke', '0002_alter_stroke_gender_alter_stroke_heart_disease_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stroke',
            name='avg_glucose_level',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)]),
        ),
    ]
