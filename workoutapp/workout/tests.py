from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

import datetime

from models import Workout

# Create your tests here.

class WorkoutModelTest(TestCase):

    def workout_created_past_date(workout_name):
        
        """
        Create a workout with a date in the past

        """
        time = timezone.now() - datetime.timedelta(days=30)
        return Workout.objects.create(workout_name=workout_name, workout_date=time)

    def workout_created_future_date(workout_name):
        
        """
        Create a workout with a date in the future

        """
        time = timezone.now() + datetime.timedelta(days=30)
        return Workout.objects.create(workout_name=workout_name, workout_date=time)
    
    def workout_created_today(workout_name, days):
        
        """
        Create a workout with today's date

        """
        time = timezone.now() - datetime.timedelta(days=days)
        return Workout.objects.create(workout_name=workout_name, workout_date=time)