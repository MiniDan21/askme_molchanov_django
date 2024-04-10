from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.db.models import Count


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    avatar = models.ImageField(null=True, blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    def __str__(self) -> str:
        return self.name


class QuestionManager(models.Manager):
    def get_new(self):
        return Question.manager.all().order_by('-create_at')

    def get_hot(self):
        return self.get_queryset().order_by('-likes')
    
    def get_by_tag(self, tag):
        return Question.manager.get(name=tag)


class Like(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    _likes = models.IntegerField(default=0)

    def like(self):
        self._likes += 1

    def dislike(self):
        self._likes -= 1

    def __str__(self) -> str:
        return f'Abstract Like Object'


class QuestionLike(Like):
    def __str__(self) -> str:
        return f'Question_{self.author}_{self._likes}'


class AnswerLike(Like):
    def __str__(self) -> str:
        return f'Answer_{self.author}_{self._likes}'


class Question(models.Model):
    avatar = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.OneToOneField(QuestionLike, on_delete=models.CASCADE)

    manager = QuestionManager()

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    likes = models.OneToOneField(AnswerLike, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.question}_answer_{self.author}'
