from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render, redirect


def index(request: HttpRequest):
    from random import randint, sample

    user = request.COOKIES.get('user', False)
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

    return render(request, "index.html", {"questions": questions, "user": user})

def question(request, id):
    return render(request, "question.html")

def tag(request, tag_name):
    return render(request, "tag.html")

def hot(request):
    return render(request, "hot.html")

def signup(request):
    return render(request, "signup.html")

def login(request):
    # ВРЕМЕННО
    response = redirect('index', permanent=False) # replace redirect with HttpResponse or render
    user = dict(
        auth=True,
        nickname='Travolta',
    )
    response.cookies['user'] = user
    return response

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