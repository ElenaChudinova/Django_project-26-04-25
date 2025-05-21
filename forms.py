from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from .models import Product


class YourForm(forms.Form):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                       'радар', ]


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductForm(YourForm, StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ["views_counter", ]

    def clean_product_name(self):
        product_name = self.cleaned_data['product_name']
        for forbidden_word in self.forbidden_words:
            if forbidden_word in product_name.lower():
                raise ValidationError('Запрещенное слово')

        return product_name

    def clean_description(self):
        description = self.cleaned_data['description']
        for forbidden_word in self.forbidden_words:
            if forbidden_word in description.lower():
                raise ValidationError('Запрещенное слово')

        return description
