from django.views.generic import (
    ListView,
    UpdateView,
    CreateView,
    DeleteView,
)
from django.views.generic.edit import FormView

from rest_framework import generics

# locale imports
from .forms import SurveyForm

from .models import Survey, Question, Answer, UserAnswer

from .serializers import (
    SurveySerializer,
    QuestionSerializer,
    AnswerSerializer,
    UserAnswerSerializer,
)


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
    success_url = '/'

    template_name = 'create_survey.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SurveyDeleteView(DeleteView):
    model = Survey
    success_url = '/'

    template_name = 'delete_survey.html'


class SurveyAPIView(generics.ListAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


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


class QuestionAPIView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        pk = self.request.query_params.get('id')
        return Question.objects.filter(pk=pk)


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


class AnswerAPIView(generics.ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        pk = self.request.query_params.get('id')
        return Answer.objects.filter(pk=pk)


class UserAnswerAPIView(generics.ListCreateAPIView):
    serializer_class = UserAnswerSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        return UserAnswer.objects.filter(user_id=str(user_id))
