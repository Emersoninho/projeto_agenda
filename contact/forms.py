from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label='Primeiro nome',
        help_text='Texto de ajuda para seu usuario'
    )
    # def __init__(self, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)

    #     self.fields['first_name'].widget.attrs.update({
    #         'class': 'classe-a classe-b',
    #         'placeholder': 'Aqui veio do init',
    #     })

    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone')

        # widgets = {'first_name': forms.TextInput(
        #     attrs={
        #         'class': 'classe-a classe-b',
        #         'placeholder': 'Escreva aqui',
        #     }
        # )}

    def clean(self):
        #cleaned_data = self.cleaned_data

        self.add_error('first_name', ValidationError('mensagem de erro', code='invalid'))
        return super().clean()   
    
    
    def clean(self):
        #cleaned_data = self.cleaned_data

        self.add_error('first_name', ValidationError('mensagem de erro 2', code='invalid'))
        return super().clean() 