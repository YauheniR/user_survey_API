from django.contrib import admin
from survey.models import SurveyModel, AnswerModel
from survey.models import QuestionModel


class QuestionInstanceInLine(admin.TabularInline):
    model = QuestionModel
    extra = 0
    fields = ('type', 'content',)


class SurveyAdmin(admin.ModelAdmin):
    inlines = (QuestionInstanceInLine,)
    fields = ('title', 'description', ('start_date', 'end_date',),)


class QuestionAdmin(admin.ModelAdmin):
    fields = ('type', 'content', 'survey')


class AnswerAdmin(admin.ModelAdmin):
    pass


admin.site.register(AnswerModel, AnswerAdmin)
admin.site.register(SurveyModel, SurveyAdmin)
admin.site.register(QuestionModel, QuestionAdmin)
