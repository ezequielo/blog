from django import forms

class CreateAccountForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
#     TODO
#     def send_email(self):
#         # send email using the self.cleaned_data dictionary
#         pass