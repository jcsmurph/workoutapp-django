from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.edit import FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import ListView, DetailView

from workout.forms import ExerciseForm, WorkoutForm
from workout.models import Exercise, Workout

# Instantiate the Workout Model
class WorkoutIndexView(ListView):

    model = Workout
    template_name = 'workout/index.html'
    context_object_name = "workouts"
    pk_url_kwarg = "workout"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workoutform'] = WorkoutForm()
        return context

# Creates and processes Workout Form
class WorkoutFormView(FormView):

    model = Workout
    template_name = 'workout/index.html'
    form_class = WorkoutForm

    def get_success_url(self):
        return reverse('workout:index')

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

# Instantiate the Index
class WorkoutIndexNavi(View):

    def get(self, request, *args, **kwargs):
        view = WorkoutIndexView.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = WorkoutFormView.as_view()
        workoutform = WorkoutForm(request.POST)
        if workoutform.is_valid():
            workoutform.save()
        return view(request, *args, **kwargs)

# Instantiate the Workout Details
class ExerciseDetail(DetailView):

    model = Workout
    template_name = 'workout/exercise_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exerciseform'] = ExerciseForm(initial={'workout': self.object})
        return context

# Creates and processes Exercise Form
class ExerciseFormView(SingleObjectMixin, FormView):

    model = Workout
    template_name = 'workout/exercise_detail.html'
    form_class = ExerciseForm

    def get_success_url(self):
        return reverse('workout:exercise_detail', kwargs={'pk':self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

# Used as URL pointer for workout_details
# Utilizes GET (ExerciseDetail) and POST (ExerciseFormView)
class ExerciseDetailNavigation(View):

    def get(self, request, *args, **kwargs):
        view = ExerciseDetail.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = ExerciseFormView.as_view()
        exerciseform = ExerciseForm(request.POST)
        exerciseform.instance.workout = Workout.objects.get(id=self.kwargs['pk'])
        if exerciseform.is_valid():
            exerciseform.save()
        return view(request, *args, **kwargs)


# Deletes exercises
def DeleteExercise(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        exercise.delete()
        return redirect(request.META.get('HTTP_REFERER'))

# Deletes Workouts
def DeleteWorkout(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        workout.delete()
        return redirect('/workout')