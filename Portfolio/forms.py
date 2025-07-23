from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        required=True, 
        label='Your Name', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'})
    )

    email = forms.EmailField(
        required=True, 
        label='Your Email', 
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )

    subject = forms.CharField(
        max_length=200, 
        required=True, 
        label='Subject', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter the subject'})
    )

    message = forms.CharField(
        required=True, 
        label='Your Message',
        widget=forms.Textarea(attrs={'placeholder': 'Enter your message'})
    )