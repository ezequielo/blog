from django import forms

class CreateAccountForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
#     TODO
#     def send_email(self):
#         # send email using the self.cleaned_data dictionary
#         pass


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
#     TODO
#     def send_email(self):
#         # send email using the self.cleaned_data dictionary
#         pass


# class LoginForm(form.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput())
    
    