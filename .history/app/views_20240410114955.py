from typing import Dict
from random import randint, sample

from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, PageNotAnInteger


authed = True
TAGS = ['IT', 'JS', 'C++', 'Python', 'Django', 'Golang']
QUESTIONS = [{
        'title': f'title {i}',
        'id': i,
        'text': f'text {i}',
        'answers': f'answers {randint(0, 6)}',
        'tags': [{'name': tag} for tag in sample(TAGS, randint(1, 3))],
        'likes': randint(10, 20),
        'avatar': '../static/img/alter_question_avatar.jpg',
    } for i in range(1,30)]

def paginate(
        request: HttpRequest, 
        page_file, 
        object_list, 
        per_page=10, 
        content: Dict = {}
    ):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(object_list, 5)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        return render(request, page_file, {page_obj})
    content['questions'] = page_obj
    page = render(request, page_file, content)
    return page

def index(request: HttpRequest):
    return render(request, "index.html", {"questions": QUESTIONS, "authed": authed})

def question(request, id):
    return render(request, "question.html", {"authed": authed})

def tag(request, tag_name):
    QUESTIONS['tags'] = [{'name': tag_name}]
    
    return render(request, "tag.html", {'questions': QUESTIONS, 'tag': tag_name, "authed": authed})

def hot(request):
    return render(
        request, 
        "hot.html", 
        {
            "authed": authed, 
            "questions": sorted(QUESTIONS, key=lambda x: x['likes'])[::-1]
        },
    )

def signup(request):
    return render(request, "signup.html")

def login(request: HttpRequest):
    global authed
    authed = True
    
    return render(request, "login.html")

def ask(request):
    return render(request, "ask.html", {"authed": authed})

def logout(request: HttpRequest):
    global authed 
    authed = False
    return redirect('index', permanent=False)

def settings(request):
    return render(request, "settings.html", {"authed": authed})