from django import forms
from community import models

class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.CommunityAnswer
        fields = ("content", 'question', 'farmer')
