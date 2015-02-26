from django.contrib import admin
from polls.models import Question,Choice
# Register your models here.
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    filedsets = [
        (None,{'field':['question_text']}),
        ('Date infomation',{'field':['pub_date'],'class':['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text','pub_date')
    list_filter = ['pub_date']
admin.site.register(Question,QuestionAdmin)