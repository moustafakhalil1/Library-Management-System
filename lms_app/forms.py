from dataclasses import fields
from django import forms
from .models import books,category

class bookforms(forms.ModelForm):
    class Meta:
        model= books
        fields= [
             'Title',
             'author',
             'photo_book',
             'photo_author',
             'pages',
             'price',
             'rental_day_pric',
             'rental_priod',
             'total_pric',
             'status',
             'category',

        ]
        widgets = {
              'Title':forms.TextInput(attrs={'class':'form-control'}),
              'author':forms.TextInput(attrs={'class':'form-control'}),
              'photo_book':forms.FileInput(attrs={'class':'form-control'}),
              'photo_author':forms.FileInput(attrs={'class':'form-control'}),
              'pages':forms.NumberInput(attrs={'class':'form-control'}),
              'price':forms.NumberInput(attrs={'class':'form-control'}),
              'rental_day_pric':forms.NumberInput(attrs={'class':'form-control', 'id':'rentalpric'}),
              'rental_priod':forms.NumberInput(attrs={'class':'form-control', 'id':'rentaldays'}),
              'total_pric':forms.NumberInput(attrs={'class':'form-control', 'id':'totalpric'}),
              'status':forms.Select(attrs={'class':'form-control'}),
              'category':forms.Select(attrs={'class':'form-control'}),
        }
       
class categoryforms(forms.ModelForm):
    class Meta:
        model= category
        fields = ['name']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
        }
