from django.db import models
from django.conf import settings


class Survey(models.Model):
    """Survey model

    Fields
    ------
    title : CharField
        Survey title
    start_date : DateTimeField
        Survey start date
    end_date : DateTimeField
        Survey end date
    description : TextField
        Survey description

    """

    title = models.CharField(
        verbose_name='Название',
        max_length=255,
    )
    start_date = models.DateTimeField(
        verbose_name='Дата старта',
    )
    end_date = models.DateTimeField(
        verbose_name='Дата окончания',
    )
    description = models.TextField(
        verbose_name='Описание',
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(models.Model):
    """Question model

    Fields
    ------
    survey : ForeignKey
        Survey model
    text : CharField
        Question text
    type_question : CharField
        Question type

    """

    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE,
        verbose_name='Опрос',
    )
    text = models.CharField(
        verbose_name='Текст вопроса',
        max_length=255,
    )
    TYPE_CHOICES = (
        ('text_ans', 'Текстовый ответ'),
        ('one_ans', 'Один ответ'),
        ('some_ans', 'Несколько ответов'),
    )
    type_question = models.CharField(
        max_length=8,
        choices=TYPE_CHOICES,
    )


class Answer(models.Model):
    """Answer model

    Fields
    ------
    question : ForeignKey
        Question model
    text : CharField
        Answer text

    """

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name='Вопрос',
    )
    text = models.CharField(
        verbose_name='Текст ответа',
        max_length=255,
    )


class UserAnswer(models.Model):
    """User answer model

    Fields
    ------
    user : ForeignKey
        User model
    question : ForeignKey
        Question model
    answer : ForeignKey
        Answer model
    created : DateTimeField
        Date the record was created

    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.DO_NOTHING,
    )
    answer = models.ForeignKey(
        Answer,
        on_delete=models.DO_NOTHING,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.choice.title
