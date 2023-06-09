# Generated by Django 4.1 on 2023-03-24 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_idea_downvote_idea_upvote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='downvote',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='upvote',
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_liked', models.DateTimeField(default=django.utils.timezone.now)),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.idea')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_disliked', models.DateTimeField(default=django.utils.timezone.now)),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.idea')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
