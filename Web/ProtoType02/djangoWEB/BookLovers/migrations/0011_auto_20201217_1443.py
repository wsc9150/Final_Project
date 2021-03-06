# Generated by Django 3.0.3 on 2020-12-17 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookLovers', '0010_auto_20201217_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teenagerbook',
            name='describe',
        ),
        migrations.RemoveField(
            model_name='teenagerbook',
            name='keyword',
        ),
        migrations.AddField(
            model_name='teenagerbook',
            name='average_rating',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='teenagerbook',
            name='intro',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='teenagerbook',
            name='num_pages',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='teenagerbook',
            name='text_reviews_count',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='teenagerbook',
            name='loan_count',
            field=models.TextField(default=''),
        ),
    ]
