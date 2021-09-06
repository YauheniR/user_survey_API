from django.urls import path
from survey.views import SurveysViews
from survey.views import SurveyViews

urlpatterns = [
    path("", SurveysViews.as_view()),
    path("<int:survey_id>/", SurveyViews.as_view())
    ]
