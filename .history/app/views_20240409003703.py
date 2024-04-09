from django.shortcuts import get_object_or_404, render


def index(request):
    from random import randint, choice
    questions = []
    TAGS = ['IT', 'JS', 'C++', 'Python', 'Django', 'Golang']
    for i in range(1,30):
        tags = [{'name': choice(TAGS)} for tag in range(randint(1, 3))]
        questions.append({
            'title': f'title {i}',
            'id': i,
            'text': f'text {i}',
            'answers': f'answers {randint(0, 10)}',
            'tags': tags,
            'likes': randint(-10, 10),
            'avatar': '../static/img/alter_question_avatar.jpg',
        })
    return render(request, "index.html", {"questions": questions})
