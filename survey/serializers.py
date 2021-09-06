from rest_framework import serializers
from survey.models import SurveyModel, QuestionModel


class SurveysSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyModel
        fields = '__all__'


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = '__all__'
