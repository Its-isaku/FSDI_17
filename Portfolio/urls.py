
#? Import necessary modules
from django.urls import path
from .views import (
    homePageView,
    experiencePageView,
    contactPageView
)

#? URL patterns for the Portfolio app
urlpatterns = [
    path('', homePageView, name='home'),                          #* Home page URL pattern
    path('experience/', experiencePageView, name='experience'),   #* Experience page URL pattern
    path('contact/', contactPageView, name='contact'),            #* Contact page URL pattern
]
