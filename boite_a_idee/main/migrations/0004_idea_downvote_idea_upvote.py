# Generated by Django 4.1 on 2023-03-23 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_idea_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='downvote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='idea',
            name='upvote',
            field=models.IntegerField(default=0),
        ),
    ]
