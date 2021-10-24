from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.


questions = [
    {
        "title": f'Title {i}',
        "text": f'Content {i}',
        "num": i,
    } for i in range(100)
]


def index(request):
    paginator = Paginator(questions, 10)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "index.html", {'questions': content})


def hot(request):
    return render(request, "hot.html", {})


def question(request):
    return render(request, "question.html", {})
