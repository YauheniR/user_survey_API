from django.urls import include
from django.urls import path
from survey.views import SurveysViews
from survey.views import AnswersViews
from survey.views import SurveyResponsesViews
from survey.views import SurveyViews

urlpatterns = [
    path("answers/", AnswersViews.as_view()),
    path("", SurveysViews.as_view()),
    path(
        "<int:survey_id>/",
        include(
            [
                path("", SurveyViews.as_view()),
                path("answer/", SurveyResponsesViews.as_view()),
            ]
        ),
    ),
]
