# Generated by Django 4.2.5 on 2023-09-19 09:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stroke',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)])),
                ('gender', models.IntegerField(choices=[('0', 'Female'), ('1', 'Male'), ('2', 'Others')])),
                ('hypertension', models.BooleanField(default=False)),
                ('heart_disease', models.BooleanField(default=False)),
                ('avg_glucose_level', models.FloatField()),
                ('bmi', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)])),
                ('smoking_status', models.IntegerField(choices=[('0', 'Formerly Smoked'), ('1', 'Never Smoked'), ('2', 'Smokes')])),
            ],
        ),
    ]
