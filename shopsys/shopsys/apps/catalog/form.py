from django import forms
from .models import Product

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []

    def clean_price(self):
        if self.clean_data['price'] <= 0:
            raise forms.ValidationError('价格必须大于0')
        return self.clean_data['price']

