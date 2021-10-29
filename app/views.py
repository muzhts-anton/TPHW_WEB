from django.shortcuts import render
from django.core.paginator import Paginator


questions = [
    {
        "title": f'Question title {i + 1}',
        "text": f'Question content {i + 1}',
        "id": i,
    } for i in range(100)
]


def index(request):
    paginator = Paginator(questions, 10)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "index.html", {'questions': content})


def bender(request):
    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "tag.html", {'questions': content})


answers = [
    {
        "title": f'Answer title {i + 1}',
        "text": f'Answer content {i + 1}',
        "id": i,
    } for i in range(7)
]


def question(request):
    paginator = Paginator(answers, 2)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "question.html", {"question": questions[5], "answers": content})


def ask(request):
    return render(request, "ask.html", {})


def settings(request):
    return render(request, "settings.html", {})


def login(request):
    return render(request, "login.html", {})


def register(request):
    return render(request, "register.html", {})
