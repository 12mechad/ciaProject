# Generated by Django 4.1.4 on 2024-04-08 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('immobilier', '0006_qualite_rejoindrecontact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qualite',
            old_name='name',
            new_name='qualite',
        ),
    ]