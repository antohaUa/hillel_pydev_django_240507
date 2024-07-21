from django import forms


class LoginForm(forms.Form):
    """Login Django form."""
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Login', 'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Your Password', 'class': 'form-control'}))


class RegisterForm(forms.Form):
    """Register User Django form."""
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Login', 'class': 'form-control'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'your_email@example.com', 'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Your Password', 'class': 'form-control'}))
