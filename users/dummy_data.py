import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

import random
from faker import Faker
from accounts.models import CustomUser




def generate_dummy_users(num=10):
    fake = Faker()
    
    for _ in range(num):
        # Generate a random image URL using an online service
        random_image_url = f'https://picsum.photos/200/300?random={random.randint(1, 1000)}'
        
        CustomUser.objects.create(
            email=fake.unique.email(),
            username=fake.user_name(),
            is_active=random.choice([True, False]),
            is_staff=random.choice([True, False]),
            image=random_image_url,  # Assign random image URL
        )

# Generate 10 dummy users
generate_dummy_users(10)
