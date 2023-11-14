# Generated by Django 4.2.6 on 2023-10-25 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_featured'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='post.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='comment_count',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
