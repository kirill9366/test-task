from django.db import models


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
        verbose_name='Тип вопроса',
        max_length=8,
        choices=TYPE_CHOICES,
    )

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


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

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class UserAnswer(models.Model):
    """User answer model

    Fields
    ------
    user_id : CharField
        user identificator
    question : ForeignKey
        Question model
    answer : ForeignKey
        Answer model
    created : DateTimeField
        Date the record was created

    """

    user_id = models.CharField(
        verbose_name='Идентификатор пользователя',
        max_length=10,
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.DO_NOTHING,
        verbose_name='Вопрос',
    )
    answer = models.ForeignKey(
        Answer,
        on_delete=models.DO_NOTHING,
        verbose_name='Ответ',
        null=True,
        blank=True,
    )
    text_answer = models.CharField(
        max_length=255,
        verbose_name='Текст ответа',
        null=True,
        blank=True,
    )
    created = models.DateTimeField(
        verbose_name='Создано',
        auto_now_add=True,
    )

    def __str__(self):
        return self.choice.title
