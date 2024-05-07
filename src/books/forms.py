from django import forms
from .models import BookTitle


class BookTitleForm(forms.ModelForm):
    class Meta:
        model = BookTitle
        fields = ('title','publisher', 'author')

    def clean (self):
        title = self.cleaned_data.get('title')

        if len(title) <5:
            self.add_error('title', 'the title is too short')

        return self.cleaned_data



