from django.shortcuts import get_object_or_404, render


def index(request):
    questions = []
    for i in range(1,30):
        questions.append({
            'title': 'title ' + str(i),
            'id': i,
            'text': 'text' + str(i)
        })
    return render(request, "index.html", {"questions": questions})
