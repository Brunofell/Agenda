# Generated by Django 5.1.6 on 2025-02-20 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
