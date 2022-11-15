from django import views
from django.urls import path

from .views import ExerciseDetailNavigation,WorkoutIndexNavi
from workout.views import DeleteExercise, DeleteWorkout

app_name = 'workout'

urlpatterns = [
    path('', WorkoutIndexNavi.as_view(), name='index'),
    path('<int:pk>/', ExerciseDetailNavigation.as_view(), name='exercise_detail'),
    path('delete_exercise/<int:pk>', DeleteExercise, name='delete_exercise'),
    path('delete_workout/<int:pk>', DeleteWorkout, name='delete_workout')
]