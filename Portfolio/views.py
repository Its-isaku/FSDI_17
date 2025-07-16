
#?  Import necessary modules
from django.shortcuts import render

#? Function to handle the home page view
def homePageView(request):
    return render(request, 'pages/home.html')  #* Render the home template
    
#? Function to handle the Experience page view
def experiencePageView(request):
    return render(request, 'pages/experience.html')  #* Render the experience template
    
#? Function to handle the Contact page view
def contactPageView(request):
    return render(request, 'pages/contact.html')  #* Render the contact template