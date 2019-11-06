from django.forms import ModelForm, TextInput, EmailInput, DateInput, FileInput, Textarea
from django.contrib.auth.models import User

from map.models import Answer


class AddAnswer(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']
        exclude = ['map', 'group']
        widgets =  {
            'answer': Textarea(attrs={'placeholder': '"!;?*#',
                                'class': 'form-control',
                                             'cols': '100%', 'rows': '2'}),
        }