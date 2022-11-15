# Generated by Django 4.1.3 on 2022-11-09 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('movement_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('body_part', models.CharField(choices=[('Quads', 'Quads'), ('Hamstrings', 'Hamstrings'), ('Calves', 'Calves'), ('Chest', 'Chest'), ('Back', 'Back'), ('Shoulders', 'Shoulders'), ('Biceps', 'Biceps'), ('Triceps', 'Triceps')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout_name', models.CharField(max_length=200)),
                ('workout_date', models.DateTimeField(verbose_name='Date of Workout')),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sets', models.IntegerField(default=0)),
                ('reps', models.IntegerField(default=0)),
                ('movement', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='workout.movement')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workout.workout')),
            ],
        ),
    ]
