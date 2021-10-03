from django.test import TestCase

# locale imports
from questionnaire.views import (
    AnswerAPIView,
    AnswerCreateView,
    AnswerDeleteView,
    AnswerUpdateView,
    CreateView,
    DeleteView,
    FormView,
    ListView,
    QuestionAPIView,
    QuestionCreateView,
    QuestionDeleteView,
    QuestionUpdateView,
    SurveyAPIView,
    SurveyDeleteView,
    SurveyFormView,
    SurveyListView,
    SurveyUpdateView,
    UpdateView,
    UserAnswerAPIView,
)
from questionnaire.models import (
    Survey,
    Question,
    Answer,
    UserAnswer,
)


class AnswerAPIViewTestCase(TestCase):

    fixtures = [
        'survey.json',
        'question.json',
        'answer.json',
        'user_answer.json',
    ]
