from django.shortcuts import render
from django.core.paginator import Paginator
from app import models


def paginate(data, request, per_page=10):
    paginator = Paginator(data, per_page)
    page = request.GET.get('page')
    pag_questions = paginator.get_page(page)
    return pag_questions

# questions = [
#     {
#         "title": f'Question title {i + 1}',
#         "text": f'Question content {i + 1}',
#         "id": i,
#     } for i in range(100)
# ]


def index(request):
    questions = models.Question.objects.new_questions()
    tags = models.Tag.objects.all()[0:8]
    profiles = models.Profile.objects.all()[0:5]
    content = paginate(questions, request)
    return render(request, "index.html", {'questions': content, 'tags': tags, 'profiles': profiles})


# def bender(request):
#     content = paginate(questions, request, 5)
#     return render(request, "tag.html", {'questions': content})


# # answers = [
# #     {
# #         "title": f'Answer title {i + 1}',
# #         "text": f'Answer content {i + 1}',
# #         "id": i,
# #     } for i in range(7)
# # ]


# def question(request):
#     content = paginate(answers, request, 2)
#     return render(request, "question.html", {"question": questions[5], "answers": content})


# def ask(request):
#     return render(request, "ask.html", {})


# def settings(request):
#     return render(request, "settings.html", {})


# def login(request):
#     return render(request, "login.html", {})


# def register(request):
#     return render(request, "register.html", {})
