import os

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Project


def index(request):
    projects = Project.objects.order_by('id')
    paginator = Paginator(projects, 3)
    for page in paginator:
        print(list(page))
    return render(
        request,
        "index.html",
        {
            'project_rows': [
                [
                    {
                        'title': project.title,
                        'description': project.description,
                        'url': project.url,
                        'image': project.image,
                    } for project in project_row
                ] for project_row in paginator
            ]
        }
    )


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('contactName')
        email = request.POST.get('contactEmail')
        message = request.POST.get('contactMessage')

        formatted_message = f"""
            FROM: {name}
            EMAIL: {email}
            MESSAGE: {message}
        """

        mail_command = f'echo "{formatted_message}" | s-nail -s "{name}" yegor@ystepanoff.net'
        os.system(mail_command)
    return ''

