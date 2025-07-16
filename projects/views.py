#?  Import necessary modules
from django.shortcuts import render
from . import models

#? Function to handle the Projects page view
def projectsPageView(request):
    projects = models.Project.objects.all()  #* Fetch all projects from the database
    context = {
        'projects': projects,                 #* Context variable to pass projects to the template
    }
    return render(request, 'projects/project_list.html', context)
