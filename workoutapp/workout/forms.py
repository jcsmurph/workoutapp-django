from django import forms
from django.forms import ModelForm
from workout.models import Exercise, Workout

class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = "__all__"

class DeleteExerciseForm(forms.Form):
    pk = forms.IntegerField()


class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = "__all__"

class DeleteWorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = "__all__"
