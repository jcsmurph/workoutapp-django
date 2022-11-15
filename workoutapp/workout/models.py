import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Stores movements
class Movement(models.Model):

    class BodyPart(models.TextChoices):
        QUADS = "Quads", ("Quads")
        HAMSTRINGS = "Hamstrings", ("Hamstrings")
        CALVES = "Calves", ("Calves")
        CHEST = "Chest", ("Chest")
        BACK = "Back", ("Back")
        SHOULDERS = "Shoulders", ("Shoulders")
        BICEPS = "Biceps", ("Biceps")
        TRICEPS = "Triceps", ("Triceps")

    movement_name = models.CharField(max_length=200, primary_key=True)
    body_part = models.CharField(max_length=200, choices=BodyPart.choices)

    def __str__(self) -> str:
        return self.movement_name

# Stores the Workouts and associated Exercises
class Workout(models.Model):
    workout_name = models.CharField(max_length=200)
    workout_date = models.DateField("Date of Workout", default=datetime.date.today)
    
    def __str__(self) -> str:
        return self.workout_name

# Stores movements and the associated Sets x Reps
class Exercise(models.Model):
    movement = models.ForeignKey(Movement, on_delete=models.PROTECT)
    sets = models.IntegerField(
                default=1, 
                validators=[
                    MaxValueValidator(100),
                    MinValueValidator(1)
        ])
    reps = models.IntegerField(
                default=1, 
                validators=[
                    MaxValueValidator(100),
                    MinValueValidator(1)
        ])
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, editable=False)
    
    def __str__(self) -> str:
        return self.movement.movement_name