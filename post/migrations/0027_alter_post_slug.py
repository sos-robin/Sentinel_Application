# Generated by Django 4.2.6 on 2023-11-01 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0026_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]