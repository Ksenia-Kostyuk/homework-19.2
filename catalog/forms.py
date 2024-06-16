from django.forms import ModelForm, forms, BooleanField

from catalog.models import Product, Version


class StyleFormMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def cleaned_data(self):
        cleaned_name = self.cleaned_data['name']
        cleaned_description = self.cleaned_data['description']
        list_taboo = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for taboo in list_taboo :
            if taboo in cleaned_name and list_taboo in cleaned_description:
                raise forms.ValidationError(f'Вы ввели запрещенное слово')
        return cleaned_name


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
