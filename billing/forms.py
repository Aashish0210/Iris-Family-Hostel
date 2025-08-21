from django import forms

class GenerateInvoicesForm(forms.Form):
    month = forms.IntegerField(min_value=1, max_value=12, initial=1, help_text='1-12')
    year = forms.IntegerField(min_value=2000, max_value=2100, initial=2025)
    amount = forms.DecimalField(max_digits=10, decimal_places=2, initial=5000.00, help_text='Base amount per kid')
    vat_rate = forms.DecimalField(max_digits=5, decimal_places=2, initial=13.00, help_text='VAT % (e.g. 13 for 13%)')
