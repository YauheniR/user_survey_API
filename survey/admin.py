from django.contrib import admin
from survey.models import SurveyModel
from survey.models import QuestionModel


class QuestionInstanceInLine(admin.TabularInline):
    model = QuestionModel
    extra = 0
    fields = (
        "type",
        "content",
    )


class SurveyAdmin(admin.ModelAdmin):
    inlines = (QuestionInstanceInLine,)
    fields = (
        "title",
        "description",
        (
            "start_date",
            "end_date",
        ),
    )


admin.site.register(SurveyModel, SurveyAdmin)
