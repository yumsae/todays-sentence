# Generated by Django 4.0.6 on 2022-08-19 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buildapp', '0002_sentence'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentence',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='sentence',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sentence', to=settings.AUTH_USER_MODEL),
        ),
    ]
