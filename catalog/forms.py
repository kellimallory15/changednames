from django import forms


class OrderForm(forms.Form):
    product_name = forms.CharField(label='Product Name')
    amount = forms.DecimalField(label='Amount')