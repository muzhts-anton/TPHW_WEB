from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.


questions = [
    {
        "title": f'Title {i + 1}',
        "text": f'Content {i + 1}',
        "num": i,
    } for i in range(100)
]


def index(request):
    paginator = Paginator(questions, 10)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "index.html", {'questions': content})


def question(request):
    return render(request, "question.html", {})
