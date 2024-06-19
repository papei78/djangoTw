from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.ComboField(label="Password",widget=forms.PasswordInput)


class OTPForm(forms.FOrm):
    otp = forms.CharField(label="OTP", max_length=6)