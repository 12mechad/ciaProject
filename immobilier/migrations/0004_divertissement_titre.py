# Generated by Django 4.1.4 on 2024-03-03 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immobilier', '0003_divertissement_arrondissement_divertissement_commune_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='divertissement',
            name='titre',
            field=models.CharField(max_length=100, null=True),
        ),
    ]