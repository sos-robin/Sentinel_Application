# Generated by Django 4.2.6 on 2023-10-26 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_category_slug_alter_post_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categories',
            new_name='category',
        ),
    ]
