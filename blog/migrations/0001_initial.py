# Generated by Django 3.0.4 on 2020-03-13 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Article_id', models.IntegerField()),
                ('writer', models.CharField(max_length=20)),
                ('article_title', models.CharField(max_length=30)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.CharField(max_length=2000)),
            ],
        ),
    ]
