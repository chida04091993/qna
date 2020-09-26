from django import forms

from qna.models import Question, Answer

class AnswerForm(forms.ModelForm):

    class Meta:

        model = Answer

        fields = ['answer']