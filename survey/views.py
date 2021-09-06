from rest_framework import generics

from survey.models import SurveyModel
from survey.models import QuestionModel
from survey.serializers import SurveysSerializer
from survey.serializers import AnswerSerializer
from survey.serializers import SurveySerializer


class SurveysViews(generics.ListAPIView):
    queryset = SurveyModel.objects.all()
    serializer_class = SurveysSerializer


class SurveyViews(generics.ListAPIView):
    queryset = QuestionModel.objects.all()
    serializer_class = SurveySerializer
    lookup_field = "id"
    lookup_url_kwarg = "survey_id"

    def get_queryset(self):
        return (
            super(SurveyViews, self)
            .get_queryset()
            .filter(survey_id=self.kwargs.get("survey_id"))
        )


class AnswerViews(generics.CreateAPIView):
    serializer_class = AnswerSerializer
    lookup_field = "id"
    lookup_url_kwarg = "question_id"
