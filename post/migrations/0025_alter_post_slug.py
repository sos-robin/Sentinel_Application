# Generated by Django 4.2.6 on 2023-11-01 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0024_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
