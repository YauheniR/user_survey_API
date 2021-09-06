from rest_framework import serializers
from survey.models import SurveyModel
from survey.models import QuestionModel
from survey.models import AnswerModel


class SurveysSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyModel
        fields = "__all__"


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerModel
        fields = "__all__"
