# Generated by Django 4.1.7 on 2023-02-24 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='images',
            field=models.ManyToManyField(to='api.images'),
        ),
    ]
