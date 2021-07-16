from django.forms import ModelForm

from memoapp.models import Memo


class MemoCreationForm(ModelForm):
    class Meta:
        model = Memo
        fields = ['title', 'content', 'image']