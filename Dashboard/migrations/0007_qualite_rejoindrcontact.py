# Generated by Django 4.1.4 on 2024-04-07 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0006_interviewpresse_documentairepresse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qualite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RejoindrContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('piece', models.FileField(upload_to='piece')),
                ('message', models.TextField(blank=True, null=True)),
                ('qualite', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Dashboard.qualite')),
            ],
        ),
    ]
