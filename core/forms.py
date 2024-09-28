from django import forms
from .models import *

class DonHangForm(forms.ModelForm):
    class Meta:
        model = DonDatHang
        fields = [ 'SDT', 'DiaChi']

class LoginForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['Username', 'Pass']

class SigninForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['NameAc', 'Email', 'Phone', 'Username', 'Pass']