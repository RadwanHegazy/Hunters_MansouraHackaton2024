# Generated by Django 5.1 on 2024-12-01 11:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journey', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journey',
            name='rider',
        ),
        migrations.AddField(
            model_name='journey',
            name='riders',
            field=models.ManyToManyField(null=True, related_name='riders_driver', to=settings.AUTH_USER_MODEL),
        ),
    ]
