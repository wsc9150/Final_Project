# Generated by Django 3.0.3 on 2020-12-17 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookLovers', '0012_auto_20201217_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllBook',
            fields=[
                ('no', models.IntegerField(primary_key=True, serialize=False)),
                ('bookname', models.TextField(default='')),
                ('author', models.TextField(default='')),
                ('publisher', models.TextField(default='')),
                ('publication_year', models.TextField(default='')),
                ('isbn13', models.TextField(default='')),
                ('addition_symbol', models.TextField(default='')),
                ('vol', models.TextField(default='')),
                ('class_no', models.TextField(default='')),
                ('loan_count', models.TextField(default='')),
                ('bookImageURL', models.TextField(default='')),
                ('text_reviews_count', models.TextField(default='')),
                ('average_rating', models.TextField(default='')),
                ('num_pages', models.TextField(default='')),
                ('intro', models.TextField(default='')),
            ],
        ),
    ]