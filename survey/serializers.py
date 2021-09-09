from rest_framework import serializers
from survey.models import SurveyResponsesModel
from survey.models import SurveyModel
from survey.models import QuestionModel
from survey.models import AnswerModel


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ("id", "type", "content")


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerModel
        fields = ("answer", "question")


class SurveysSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyModel
        fields = "__all__"


class SurveySerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True)

    class Meta:
        model = SurveyModel
        fields = "__all__"


class SurveyResponsesSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    def create(self, validated_data):
        print(validated_data)
        answers_data = validated_data.pop("answers")
        print(validated_data)
        survey_response = SurveyResponsesModel.objects.create(**validated_data)

        for answer_data in answers_data:
            print(answer_data)
            AnswerModel.objects.create(response=survey_response, **answer_data)
        return survey_response

    class Meta:
        model = SurveyResponsesModel
        fields = ("user_id", "answers")
