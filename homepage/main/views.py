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
                    } for project in project_row
                ] for project_row in paginator
            ]
        }
    )
