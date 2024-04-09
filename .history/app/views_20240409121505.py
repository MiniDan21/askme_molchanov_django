from django.shortcuts import get_object_or_404, render


def index(request):
    from random import randint, choice
    questions = []
    TAGS = ['IT', 'JS', 'C++', 'Python', 'Django', 'Golang']
    for i in range(1,30):
        tags = [{'name': choice(TAGS)} for _ in range(randint(1, 3))]
        print(tags)
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
    return render(request, "tag.html")

def hot(request):
    return render(request, "hot.html")

def signup(request):
    return render(request, "signup.html")

def login(request):
    return render(request, "login.html")

def ask(request):
    return render(request, "ask.html")
