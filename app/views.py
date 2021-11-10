from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from app import models


def paginate(data, request, per_page=10):
    paginator = Paginator(data, per_page)
    page = request.GET.get('page')
    pag_questions = paginator.get_page(page)
    return pag_questions


def index(request):
    questions = models.Question.objects.new_questions()
    tags = models.Tag.objects.all()[0:8]
    profiles = models.Profile.objects.all()[0:5]
    content = paginate(questions, request)
    return render(request, "index.html", {'questions': content, 'tags': tags, 'profiles': profiles})


def bender(request, tag):
    tag = get_object_or_404(models.Tag.objects, tag=tag)
    tags = models.Tag.objects.all()[0:8]
    profiles = models.Profile.objects.all()[0:5]
    questions = tag.questions()
    content = paginate(questions, request, 5)
    return render(request, "tag.html", {'questions': content, 'tag': tag, 'tags': tags, 'profiles': profiles})


def question(request, pk):
    question = get_object_or_404(models.Question.objects, pk=pk)
    tags = models.Tag.objects.all()[0:8]
    profiles = models.Profile.objects.all()[0:5]
    answers = question.answers()
    content = paginate(answers, request, 2)
    return render(request, "question.html", {"question": question, "answers": content, 'tags': tags, 'profiles': profiles})


def ask(request):
    return render(request, "ask.html", {})


def settings(request):
    return render(request, "settings.html", {})


def login(request):
    return render(request, "login.html", {})


def register(request):
    return render(request, "register.html", {})
