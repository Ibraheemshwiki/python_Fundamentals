# Generated by Django 2.2.4 on 2021-05-25 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restfull_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shows',
            name='description',
            field=models.TextField(default='description field'),
        ),
    ]
