from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text', 'question', 'votes']
    list_filter = ['question']

admin.site.register(Question)
admin.site.register(Choice, ChoiceAdmin)
