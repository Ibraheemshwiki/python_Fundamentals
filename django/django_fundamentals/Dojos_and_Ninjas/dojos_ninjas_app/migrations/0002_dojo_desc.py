# Generated by Django 2.2.4 on 2021-05-23 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojos_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='old dojo'),
        ),
    ]