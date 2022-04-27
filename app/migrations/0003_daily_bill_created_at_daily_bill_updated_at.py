# Generated by Django 4.0.4 on 2022-04-27 14:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_daily_bill_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily_bill',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='daily_bill',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
