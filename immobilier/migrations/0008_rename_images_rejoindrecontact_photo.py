# Generated by Django 4.1.4 on 2024-04-08 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('immobilier', '0007_rename_name_qualite_qualite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rejoindrecontact',
            old_name='images',
            new_name='Photo',
        ),
    ]