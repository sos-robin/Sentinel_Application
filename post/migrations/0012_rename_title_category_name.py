# Generated by Django 4.2.6 on 2023-10-26 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_alter_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
    ]