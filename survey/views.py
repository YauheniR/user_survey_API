from rest_framework import generics
from survey.models import SurveyModel
from survey.serializers import SurveysSerializer
from survey.serializers import AnswerSerializer
from survey.serializers import SurveySerializer


class SurveysViews(generics.ListAPIView):
    queryset = SurveyModel.objects.all()
    serializer_class = SurveysSerializer


class SurveyViews(generics.RetrieveAPIView):
    queryset = SurveyModel.objects.all()
    serializer_class = SurveySerializer
    lookup_field = "id"
    lookup_url_kwarg = "survey_id"


class AnswerViews(generics.CreateAPIView):
    serializer_class = AnswerSerializer
