# Generated by Django 4.1 on 2022-09-09 10:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_staff_profile_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('name', models.CharField(max_length=200, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='staff_profile',
            name='role',
        ),
        migrations.AddField(
            model_name='staff_profile',
            name='role',
            field=models.ManyToManyField(blank=True, to='users.role'),
        ),
    ]
