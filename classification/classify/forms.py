from django import forms


class ClassifyForm(forms.Form):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}))

