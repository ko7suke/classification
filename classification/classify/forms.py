from django import forms


class PredictForm(forms.Form):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}))

