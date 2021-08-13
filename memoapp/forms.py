from django import forms
from django_summernote.widgets import SummernoteWidget

from memoapp.models import Memo


class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['title', 'content']
        widgets = {
            'content' : SummernoteWidget(),
        }

# class MultipleForm(forms.Form):
#     action = forms.CharField(max_length=60, widget=forms.HiddenInput())
#
#
# class CreateForm(MultipleForm):
#     title = forms.CharField(max_length=10, null=True)
#     content = forms.TextField()
#     created_at = forms.DateField(auto_now=True)
#
# class UpdateForm(MultipleForm):
#     title = forms.CharField(max_length=10, null=True)
#     content = forms.TextField()
#     created_at = forms.DateField(auto_now=True)
