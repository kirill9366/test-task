from rest_framework import serializers

from .models import Survey, Question, Answer, UserAnswer


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = (
            'title',
            'start_date',
            'end_date',
            'description',
            'question_set',
        )


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'survey',
            'text',
            'type_question',
            'answer_set',
        )


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = '__all__'
