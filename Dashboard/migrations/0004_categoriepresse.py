# Generated by Django 4.1.4 on 2024-04-02 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0003_editionlivre_auteur'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriePresse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]