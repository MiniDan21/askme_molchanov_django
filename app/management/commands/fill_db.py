from django.core.management import BaseCommand
from django.contrib.auth.models import User
from app.models import Profile, Question, Tag, QuestionLike, AnswerLike, Answer
from faker import Faker
import random

fake = Faker()


class Command(BaseCommand):
    help = "Fills database with fake data"

    def add_arguments(self, parser):
        parser.add_argument("ratio", type=int)

    def handle(self, *args, **kwargs):
        ratio = kwargs['ratio']
        username=fake.unique.user_name()
        email=fake.email()
        profiles = [
            Profile(
                user=User.objects.create(username=username, email=email)
            ) for _ in range(ratio)
        ]

        Profile.manager.bulk_create(profiles)
        profiles = Profile.manager.all()
        tags = [
            Tag(
                name=f"Tag {i}"
            ) for i in range(ratio)
        ]
        Tag.manager.bulk_create(tags)
        questions = []
        for _ in range(ratio * 10):
            author = random.choice(profiles)
            create_date = fake.date_time()
            title = fake.sentence(nb_words=3)
            content = fake.paragraph()
            question = Question.manager.create(author=author, created_at=create_date, title=title, text=content)
            question.tags.set(random.sample(tags, random.randint(1, 3)))
        Question.manager.bulk_create(questions)
        questions = Question.manager.all()
        answers = [
            Answer(
                author=random.choice(profiles),
                question=random.choice(questions),
                created_at=fake.date_time(),
                text=fake.paragraph(),
                is_correct=False
            ) for _ in range(ratio * 100)
        ]
        Answer.manager.bulk_create(answers)
        answers = Answer.manager.all()
        questions = Question.manager.all()
        existing_likes = set()
        desired_likes = ratio * 100
        likes_to_create = []
        while len(likes_to_create) < desired_likes:
            question = random.choice(questions)
            profile = random.choice(profiles)
            if (profile.id, question.id) not in existing_likes:
                like = QuestionLike(author=profile, question=question)
                likes_to_create.append(like)
                existing_likes.add((profile.id, question.id))
        QuestionLike.objects.bulk_create(likes_to_create)

        existing_likes = set()
        desired_likes = ratio * 100
        likes_to_create = []
        while len(likes_to_create) < desired_likes:
            answer = random.choice(answers)
            profile = random.choice(profiles)
            if (profile.id, answer.id) not in existing_likes:
                like = AnswerLike(author=profile, comment=answer)
                likes_to_create.append(like)
                existing_likes.add((profile.id, answer.id))
        AnswerLike.objects.bulk_create(likes_to_create)