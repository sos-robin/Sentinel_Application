# Generated by Django 4.2.6 on 2023-11-02 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0032_teammember_remove_about_team_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='team_description',
        ),
        migrations.AddField(
            model_name='about',
            name='team_description',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]
