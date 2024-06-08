from django import forms 

from .rental_choices import FORMAT_CHOICES


class SearchBookForm(forms.Form):
    search =  forms.CharField(widget = forms.TextInput(attrs={'placeholder' : 'search by book id '}))


class SelectedExportOptionForm(forms.Form):
    format = forms.ChoiceField(choices=FORMAT_CHOICES, widget=forms.RadioSelect)
