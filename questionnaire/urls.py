from django.urls import path

# locale imports
from .views import (
    SurveyListView,
    SurveyFormView,
    SurveyUpdateView,
    SurveyDeleteView,
    SurveyAPIView,

    QuestionCreateView,
    QuestionUpdateView,
    QuestionDeleteView,
    QuestionAPIView,

    AnswerCreateView,
    AnswerUpdateView,
    AnswerDeleteView,
    AnswerAPIView,

    UserAnswerAPIView,
)

urlpatterns = [
    # survey
    path('', SurveyListView.as_view(), name='surveys'),
    path(
        'create-survey/',
        SurveyFormView.as_view(),
        name='create_survey',
    ),
    path(
        'survey/<int:pk>/',
        SurveyUpdateView.as_view(),
        name='survey_update',
    ),
    path(
        'delete-survey/<int:pk>/',
        SurveyDeleteView.as_view(),
        name='delete_survey',
    ),
    path(
        'api/surveys/',
        SurveyAPIView.as_view(),
        name='api_survey',
    ),
    # question
    path(
        'create-question/',
        QuestionCreateView.as_view(),
        name='create_question',
    ),
    path(
        'question/<int:pk>/',
        QuestionUpdateView.as_view(),
        name='update_question',
    ),
    path(
        'delete-question/<int:pk>/',
        QuestionDeleteView.as_view(),
        name='delete_question',
    ),
    path(
        'api/questions/',
        QuestionAPIView.as_view(),
        name='api_question',
    ),
    # answer
    path(
        'create-answer/',
        AnswerCreateView.as_view(),
        name='create_answer',
    ),
    path(
        'answer/<int:pk>/',
        AnswerUpdateView.as_view(),
        name='update_answer',
    ),
    path(
        'answer-delete/<int:pk>/',
        AnswerDeleteView.as_view(),
        name='answer_delete',
    ),
    path(
        'api/answers/',
        AnswerAPIView.as_view(),
        name='api_answer',
    ),
    # user_answer
    path(
        'api/user-answers/',
        UserAnswerAPIView.as_view(),
        name='user_answer',
    ),
]
