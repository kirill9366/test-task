from django.test import TestCase

# locale imports
from questionnaire.models import (
    Survey,
    Question,
    Answer,
    UserAnswer,
)


class SurveyTestCase(TestCase):

    def test_verbose(self):
        self.assertEquals(Survey._meta.verbose_name, 'Опрос')
        self.assertEquals(Survey._meta.verbose_name_plural, 'Опросы')

    def test_title_field(self):
        title = Survey._meta.get_field('title')
        self.assertEquals(title.verbose_name, 'Название')
        self.assertEquals(title.max_length, 255)

    def test_start_date_field(self):
        start_date = Survey._meta.get_field('start_date')
        self.assertEquals(start_date.verbose_name, 'Дата старта')

    def test_end_date_field(self):
        end_date = Survey._meta.get_field('end_date')
        self.assertEquals(end_date.verbose_name, 'Дата окончания')

    def test_description(self):
        description = Survey._meta.get_field('description')
        self.assertEquals(description.verbose_name, 'Описание')


class QuestionTestCase(TestCase):

    def test_survey(self):
        survey = Question._meta.get_field('survey')
        self.assertEquals(Survey, Survey)
        self.assertEquals(survey.verbose_name, 'Опрос')

    def test_text(self):
        text = Question._meta.get_field('text')
        self.assertEquals(text.verbose_name, 'Текст вопроса')
        self.assertEquals(text.max_length, 255)

    def test_type_question(self):
        type_question = Question._meta.get_field('type_question')
        self.assertEquals(type_question.verbose_name, 'Тип вопроса')
        self.assertEquals(type_question.max_length, 8)


class AnswerTestCase(TestCase):

    def test_question(self):
        question = Answer._meta.get_field('question')
        self.assertEquals(question.verbose_name, 'Вопрос')

    def test_text(self):
        text = Answer._meta.get_field('text')
        self.assertEquals(text.verbose_name, 'Текст ответа')


class UserAnswerTestCase(TestCase):

    def test_user_id(self):
        user_id = UserAnswer._meta.get_field('user_id')
        self.assertEquals(user_id.verbose_name, 'Идентификатор пользователя')
        self.assertEquals(user_id.max_length, 10)

    def test_question(self):
        question = UserAnswer._meta.get_field('question')
        self.assertEquals(question.verbose_name, 'Вопрос')

    def test_answer(self):
        answer = UserAnswer._meta.get_field('answer')
        self.assertEquals(answer.verbose_name, 'Ответ')

    def test_text_answer(self):
        text_answer = UserAnswer._meta.get_field('text_answer')
        self.assertEquals(text_answer.verbose_name, 'Текст ответа')

    def test_created(self):
        created = UserAnswer._meta.get_field('created')
        self.assertEquals(created.verbose_name, 'Создано')
