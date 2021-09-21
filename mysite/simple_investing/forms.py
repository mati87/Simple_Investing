from django import forms
from django.forms import ModelForm
from simple_investing.models import Company
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ('company_name', 'outstanding_shares', 'share_price', 'revenue', 'expenses', 'total_assets','total_liabilities', 'current_assets','current_liabilities', 'operating_cashflows', 'capex')
        widgets = {
            'company_name':forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Company name'}),
            'outstanding_shares':forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Shares outstanding'}),
            'share_price':forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Share price'}),
            'revenue':forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Revenue'}),
            'expenses':forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Expenses'}),
            'total_assets':forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Total Assets'}),
            'total_liabilities':forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Total Liabilities'}),
            'current_assets' :forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Current Assets'}),
            'current_liabilities':forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Current Liabilities'}),
            'operating_cashflows':forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Operating Cashflows'}),
            'capex':forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Capital Expenditure'}),            
        }


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLogin(ModelForm):
    class Meta:
        model = User
        fields= ('username', 'password')

class CompanySymbol(forms.Form):
    company_symbol = forms.CharField(label='Company symbol', max_length=10,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Company symbol'}))
    