# Generated by Django 4.1.3 on 2022-11-10 18:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0003_alter_exercise_movement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='reps',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='sets',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]