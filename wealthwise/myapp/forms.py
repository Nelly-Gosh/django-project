from django import forms
from .models import Deposit, Withdrawal, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ['amount', 'plan', 'method']

    method = forms.ChoiceField(choices=[('Bitcoin', 'Bitcoin'), ('Ethereum', 'Ethereum'), ('USDT', 'USDT')])  # Example choices
    plan=forms.ChoiceField(choices=[('vip','vip'),('Bronze','Bronze'),('Diamond','Diamond')])

class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields = ['amount', 'method', 'wallet_address']

    method = forms.ChoiceField(choices=[('Bitcoin', 'Bitcoin'), ('Ethereum', 'Ethereum'), ('USDT', 'USDT')])




class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, help_text='Required')
    last_name = forms.CharField(max_length=100, required=True, help_text='Required')
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')
    country = forms.CharField(max_length=100, required=True)
    phone_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'country', 'phone_number')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                email=self.cleaned_data['email'],
                country=self.cleaned_data['country'],
                phone_number=self.cleaned_data['phone_number']
            )
        return user



