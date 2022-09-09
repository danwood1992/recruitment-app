from doctest import BLANKLINE_MARKER
from django.db import models
import uuid 
from users.models import Staff_Profile

class Vacancy(models.Model):
    owner = models.ForeignKey(Staff_Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    benefit = models.ManyToManyField('Benefit', blank=True)
    skill_and_exp = description = models.TextField(max_length=2000, null=True, blank=True)
    key_duties = models.TextField(max_length=2000, null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="Main logo.png")
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    salary = models.ManyToManyField('Salary', blank=True)
    hourlyWage = models.ManyToManyField('hourlyWage', blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    job_type = models.ManyToManyField('jobType', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    
    def __str__(self):
        return self.title



class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Salary(models.Model):
    amount = models.FloatField(null=True, blank=True, help_text="Salary", unique=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return f"{self.amount}k"

class hourlyWage(models.Model):
    amount = models.IntegerField(null=True, blank=True, help_text="Salary", unique=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return f"£{self.amount}"

class jobType(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Benefit(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
    




