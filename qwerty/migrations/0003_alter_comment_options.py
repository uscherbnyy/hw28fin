# Generated by Django 5.0.1 on 2024-01-24 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qwerty', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'задача', 'verbose_name_plural': 'задачи'},
        ),
    ]
