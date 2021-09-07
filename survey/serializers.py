from rest_framework import serializers
from survey.models import SurveyModel
from survey.models import QuestionModel
from survey.models import AnswerModel


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ("type", "content")


class SurveysSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyModel
        fields = "__all__"


class SurveySerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True)

    class Meta:
        model = SurveyModel
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerModel
        fields = "__all__"
