import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

import random
from faker import Faker
from job.models import Job, JOB_TYPES, EXPERIENCE, EDUCATION


def generate_fake_jobs(num=10):
    fake = Faker()
    for _ in range(num):
        title = fake.job()
        Job.objects.create(
            title=title,
            description=fake.paragraph(nb_sentences=10),
            job_type = random.choice([x[0]for x in JOB_TYPES]),
            education = random.choice([x[0]for x in EDUCATION]),
            experience = random.choice([x[0]for x in EXPERIENCE]),
            salary = random.randint(35000, 120000),
            position = title,
            due_date = fake.future_date(end_date='+30d'),
            user = random.randint(1,20),
            company = fake.company(),


        )
        
    
generate_fake_jobs()    