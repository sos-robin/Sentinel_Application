# Generated by Django 4.2.6 on 2023-11-13 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0037_alter_contact_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_post',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='overview',
            field=models.TextField(max_length=71),
        ),
    ]
