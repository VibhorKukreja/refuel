# Generated by Django 2.0.4 on 2018-08-30 12:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0005_fuel'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuel',
            name='transaction_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
