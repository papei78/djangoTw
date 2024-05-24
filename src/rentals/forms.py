from django import forms 


class SearchBookForm(forms.Form):
    search =  forms.CharField(widget = forms.TextInput(attrs={'placefolder' : 'search by book id ...'}))