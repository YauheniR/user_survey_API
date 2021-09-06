from django.urls import path, include
from survey.views import SurveysViews
from survey.views import AnswerViews
from survey.views import SurveyViews

urlpatterns = [
    path("", SurveysViews.as_view()),
    path("<int:survey_id>/", include(
        [
            path('', SurveyViews.as_view()),
            path('<int:question_id>', AnswerViews.as_view())
        ]
    ))
    ]
