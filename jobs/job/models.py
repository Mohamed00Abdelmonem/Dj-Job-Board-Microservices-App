from django.db import models
from django.utils import timezone
from django.utils.text import slugify


JOB_TYPES = (
    ('Intership','Intership'),
    ('PartTime','PartTime'),
    ('PartTime','PartTime'),
    ('Contract','Contract'))
       
EDUCATION = (
    ('PHD','PHD'),
    ('Master','Master'),
    ('Bachelor','Bachelor')) 

EXPERIENCE = (
    ('NoExperience','NoExperience'),
    ('Junior','Junior'),
    ('Mid-Level','Mid-Level'),
    ('Senior','Senior'))


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=20000)
    job_type = models.CharField(max_length=45, choices=JOB_TYPES)
    education = models.CharField(max_length=45, choices=EDUCATION)
    experience =models.CharField(max_length=45, choices=EXPERIENCE)
    salary = models.IntegerField(null=True , blank=True)
    position = models.CharField(max_length=100)
    due_date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)

    slug = models.SlugField(null=True, blank=True)
    user = models.IntegerField()
    company = models.CharField(max_length=40)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    

class JobApply(models.Model):
    user = models.IntegerField()
    job = models.ForeignKey(Job, related_name='applied_job', on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes')
    cover_letter = models.TextField(max_length=2000)
    applied_at = models.DateTimeField(default=timezone.now)


    def __str__(self) -> str:
        return str(self.job)

