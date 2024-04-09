from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("question/<int:id>", views.question, name="question"),
    path("tag/<str:tag_name>", views.tag, name="tag"),
    path("hot/", views.hot, name="hot"),
    # # ex: /polls/5/
    # path("<int:question_id>/", views.detail, name="detail"),
    # # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]