
#?  Import necessary modules
from django.shortcuts import render, redirect
from django.contrib import messages
from projects.models import Skill  #* Import Skill model from projects app
from .forms import ContactForm  #* Import ContactForm from forms module
from django.core.mail import send_mail  #* Import send_mail for sending emails

#? Function to handle the home page view
def homePageView(request):
    skills = Skill.objects.all()  #* Fetch all skills from the database
    context = {
        'skills': skills,         #* Context variable to pass skills to the template
    }
    return render(request, 'pages/home.html', context)  #* Render the home template with context
    
#? Function to handle the Experience page view
def experiencePageView(request):
    return render(request, 'pages/experience.html')  #* Render the experience template
    
#? Function to handle the Contact page view
def contactPageView(request):
    print(f"Request method: {request.method}")  #* Debug: show HTTP method
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                # Send email
                send_mail(
                    subject=f"Portfolio Contact: {form.cleaned_data['subject']}",
                    message=f"Email from Portfolio Page:\n\nName: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nSubject: {form.cleaned_data['subject']}\nMessage: {form.cleaned_data['message']}\n",
                    from_email='isaialmeraz2003@gmail.com',
                    recipient_list=['isaialmeraz2003@gmail.com'],
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully!')
                form = ContactForm()  #* Reset the form after successful submission
                return render(request, 'pages/contact.html', {'form': form, 'success': True})  #* Render the contact template with success message
            except Exception as e:
                messages.error(request, f'Failed to send email: {str(e)}')
        else:
            print("Invalid Form Data")
            print(f"Form errors: {form.errors}")
            return render(request, 'pages/contact.html', {'form': form, 'error': 'Please check your form data.'})
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})  #* Render the contact template with the form