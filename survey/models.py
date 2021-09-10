from django.db import models
from survey.constants import QuestionTypeEnum


class SurveyModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "survey"
        verbose_name_plural = "surveys"


class QuestionModel(models.Model):
    type = models.CharField(
        max_length=2, choices=QuestionTypeEnum.QUESTION_TYPE_CHOICES.value
    )
    content = models.TextField()
    survey = models.ForeignKey(
        SurveyModel, on_delete=models.CASCADE, related_name="question"
    )

    class Meta:
        verbose_name = "question"
        verbose_name_plural = "questions"


class SurveyResponsesModel(models.Model):
    user_uuid = models.UUIDField()
    survey = models.ForeignKey(
        SurveyModel, on_delete=models.CASCADE, related_name="response"
    )


class AnswerModel(models.Model):
    answer = models.TextField()
    question = models.ForeignKey(
        QuestionModel, on_delete=models.CASCADE, related_name="answers"
    )
    response = models.ForeignKey(
        SurveyResponsesModel, on_delete=models.CASCADE, related_name="answers"
    )

    def __str__(self) -> str:
        return self.answer

    class Meta:
        verbose_name = "answer"
        verbose_name_plural = "answers"
