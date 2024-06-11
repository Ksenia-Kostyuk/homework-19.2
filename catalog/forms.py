from django.forms import ModelForm, forms

from catalog.models import Product, Version


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_data(self):
        cleaned_name = self.cleaned_data['name']
        cleaned_description = self.cleaned_data['description']
        list_taboo = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for taboo in list_taboo:
            if taboo in cleaned_name or taboo in cleaned_description:
                raise forms.ValidationError(f'Вы ввели запрещенное слово: {taboo}. Попробуйте использовать другое')


class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
