from django.views.generic import (
    ListView,
    UpdateView,
    CreateView,
    DeleteView,
)
from django.views.generic.edit import FormView

# locale imports
from .forms import SurveyForm

from .models import Survey, Question, Answer


class SurveyListView(ListView):
    model = Survey
    context_object_name = 'surveys'

    template_name = 'surveys.html'


class SurveyUpdateView(UpdateView):
    model = Survey
    fields = [
        'title',
        'end_date',
        'description',
    ]
    success_url = '/'

    template_name = 'update_survey.html'


class SurveyFormView(FormView):
    form_class = SurveyForm

    template_name = 'create_survey.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SurveyDeleteView(DeleteView):
    model = Survey
    success_url = '/'

    template_name = 'delete_survey.html'


class QuestionCreateView(CreateView):
    model = Question
    fields = [
        'survey',
        'text',
        'type_question',
    ]
    success_url = '/'

    template_name = 'create_survey.html'


class QuestionUpdateView(UpdateView):
    model = Question
    fields = [
        'text',
        'type_question',
    ]
    success_url = '/'

    template_name = 'update_question.html'


class QuestionDeleteView(DeleteView):
    model = Question
    success_url = '/'

    template_name = 'delete_question.html'


class AnswerCreateView(CreateView):
    model = Answer
    fields = [
        'question',
        'text',
    ]
    success_url = '/'

    template_name = 'create_survey.html'


class AnswerUpdateView(UpdateView):
    model = Answer
    fields = [
        'question',
        'text',
    ]
    success_url = '/'

    template_name = 'update_answer.html'


class AnswerDeleteView(DeleteView):
    model = Answer
    success_url = '/'

    template_name = 'delete_answer.html'
