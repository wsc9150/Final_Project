# Generated by Django 3.0.3 on 2020-12-17 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookLovers', '0009_adultbook_childbook_teenagerbook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adultbook',
            name='describe',
        ),
        migrations.RemoveField(
            model_name='adultbook',
            name='keyword',
        ),
        migrations.AddField(
            model_name='adultbook',
            name='average_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='adultbook',
            name='num_pages',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='adultbook',
            name='text_reviews_count',
            field=models.IntegerField(default=0),
        ),
    ]
