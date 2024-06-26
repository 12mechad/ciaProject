# Generated by Django 4.1.4 on 2024-03-03 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('immobilier', '0002_zone_alter_divertissement_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='divertissement',
            name='arrondissement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='immobilier.arrondissement'),
        ),
        migrations.AddField(
            model_name='divertissement',
            name='commune',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='immobilier.commune'),
        ),
        migrations.AddField(
            model_name='divertissement',
            name='departement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='immobilier.departement'),
        ),
    ]
