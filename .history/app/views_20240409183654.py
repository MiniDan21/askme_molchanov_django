from random import randint, sample

from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render, redirect


def index(request: HttpRequest):
    questions = []
    TAGS = ['IT', 'JS', 'C++', 'Python', 'Django', 'Golang']
    for i in range(1,30):
        tags = [{'name': tag} for tag in sample(TAGS, randint(1, 3))]
        questions.append({
            'title': f'title {i}',
            'id': i,
            'text': f'text {i}',
            'answers': f'answers {randint(0, 6)}',
            'tags': tags,
            'likes': randint(-10, 10),
            'avatar': '../static/img/alter_question_avatar.jpg',
        })

    return render(request, "index.html", {"questions": questions})

def question(request, id):
    return render(request, "question.html")

def tag(request, tag_name):
    questions = []
    for i in range(1,10):
        questions.append({
            'title': f'title {i}',
            'id': i,
            'text': f'text {i}',
            'answers': f'answers {randint(0, 6)}',
            'tags': [{'name': tag_name}],
            'likes': randint(-10, 10),
            'avatar': '../static/img/alter_question_avatar.jpg',
        })
    return render(request, "tag.html", {'questions': questions, 'tag': tag_name})

def hot(request):
    questions = []
    TAGS = ['IT', 'JS', 'C++', 'Python', 'Django', 'Golang']
    for i in range(1,30):
        tags = [{'name': tag} for tag in sample(TAGS, randint(1, 3))]
        questions.append({
            'title': f'title {i}',
            'id': i,
            'text': f'text {i}',
            'answers': f'answers {randint(0, 6)}',
            'tags': tags,
            'likes': randint(10, 20),
            'avatar': '../static/img/alter_question_avatar.jpg',
        })

    return render(request, "hot.html", {"questions": sorted(questions, key=lambda x: x['likes'])[::-1]})


def signup(request):
    return render(request, "signup.html")

def login(request):
    return render(request, "login.html")

def ask(request):
    return render(request, "ask.html")

def logout(request: HttpRequest):
    response = redirect('index', permanent=False) # replace redirect with HttpResponse or render
    user = dict(
        auth=False,
    )
    response.cookies['user'] = user
    return response

def settings(request):
    return render(request, "settings.html")