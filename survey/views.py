from rest_framework import generics
from survey.models import SurveyModel, SurveyResponsesModel
from survey.serializers import SurveysSerializer
from survey.serializers import SurveyResponsesSerializer
from survey.serializers import SurveySerializer


class SurveysViews(generics.ListAPIView):
    queryset = SurveyModel.objects.all()
    serializer_class = SurveysSerializer


class SurveyViews(generics.RetrieveAPIView):
    queryset = SurveyModel.objects.all()
    serializer_class = SurveySerializer
    lookup_field = "id"
    lookup_url_kwarg = "survey_id"


class SurveyResponsesViews(generics.CreateAPIView):
    serializer_class = SurveyResponsesSerializer

    def perform_create(self, serializer):
        serializer.save(survey=SurveyModel.objects.get(id=self.kwargs.get("survey_id")))
