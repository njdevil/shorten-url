from django import forms
from ****.urlform.models import ShortLinks

class ShortLinksForm(forms.ModelForm):
    class Meta:
        model = ShortLinks
        fields = ('long_url',)
