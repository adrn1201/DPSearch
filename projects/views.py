from django.shortcuts import render

projects = [
    {
        "id": 1,
        "title" : "Project 1",
        "description": "lorem ipsum test test 1"
    },
    {
        "id": 2,
        "title" : "Project 2",
        "description": "lorem ipsum test test 2"
    },
    {
        "id": 3,
        "title" : "Project 3",
        "description": "lorem ipsum test test 3"
    },
]

def index(request):
    context = {"projects":projects}
    return render(request, 'projects/index.html', context)
