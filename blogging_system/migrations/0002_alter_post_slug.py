# Generated by Django 4.0.2 on 2022-04-27 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
