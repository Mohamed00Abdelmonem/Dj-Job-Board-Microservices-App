import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

import random
from faker import Faker
from posts.models import Post, PostLikes, Comment


def generate_fake_posts(num=10):
    fake = Faker()
    for _ in range(num):
        title = fake.job()
        Post.objects.create(
            title=title,
            content=fake.paragraph(nb_sentences=10),
            publish_date = fake.date(),
            auther_id = random.randint(1,20)
        )
        
    


def generate_fake_post_Likes(num=10):
    posts = Post.objects.all()
    for _ in range(num):
        PostLikes.objects.create(
            post=random.choice(posts),
            user_id =  random.randint(1,20)
            )



def generate_fake_comments(num=10):
    posts = Post.objects.all()
    fake = Faker()

    for _ in range(num):
        Comment.objects.create(
            post=random.choice(posts),
            user_id = random.randint(1,20),
            content = fake.text(),
            created_at = fake.date()
            
            )




generate_fake_posts(5)
generate_fake_post_Likes(10)
generate_fake_comments(10)
