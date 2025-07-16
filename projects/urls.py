
#? Import necessary modules
from django.urls import path
from .views import (
    projectsPageView,
)

#? URL patterns for the Projects app
urlpatterns = [
    path('projects/', projectsPageView, name='project_list'),         #* Projects page URL pattern
]
