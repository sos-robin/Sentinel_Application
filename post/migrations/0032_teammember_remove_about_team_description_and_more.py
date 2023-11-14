# Generated by Django 4.2.6 on 2023-11-02 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0031_alter_about_latest_news_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(upload_to='')),
                ('team_description', models.TextField()),
                ('team_member_desription', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='about',
            name='team_description',
        ),
        migrations.RemoveField(
            model_name='about',
            name='team_member_name',
        ),
        migrations.RemoveField(
            model_name='about',
            name='team_member_profile_pic',
        ),
        migrations.RemoveField(
            model_name='about',
            name='team_member_title',
        ),
    ]
