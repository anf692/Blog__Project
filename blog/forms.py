from django.forms import ModelForm
from django import forms
from .models import Post

#class pour creer le formulaire genere par django(plus securisé que les formulairs personnalisé avec html)
class formulaire(ModelForm):
    class Meta:
        model= Post
        fields=['title','content']
        widgets = {
            'title': forms.TextInput(
                attrs = {
                    'placeholder': 'Entrez le titre article',
                    'class':'form-control'
                }
            ),

            'content': forms.TextInput(
                attrs={
                    'placeholder': 'Entrez votre contenue',
                    'class':'form-control'
                }
            ),
        
        }
