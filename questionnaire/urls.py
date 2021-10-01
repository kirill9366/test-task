from django.urls import path

# locale imports
from .views import (
    SurveyListView,
    SurveyFormView,
    SurveyUpdateView,
    SurveyDeleteView,
    QuestionCreateView,
    QuestionUpdateView,
    QuestionDeleteView,
    AnswerCreateView,
    AnswerUpdateView,
    AnswerDeleteView,
)

urlpatterns = [
    path('', SurveyListView.as_view(), name='surveys'),
    path(
        'create-survey/',
        SurveyFormView.as_view(
            success_url='/'
        ),
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
    )
]
