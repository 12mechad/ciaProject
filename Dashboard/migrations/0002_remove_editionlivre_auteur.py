# Generated by Django 4.1.4 on 2024-03-22 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='editionlivre',
            name='auteur',
        ),
    ]