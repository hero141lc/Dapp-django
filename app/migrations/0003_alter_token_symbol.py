# Generated by Django 4.0.4 on 2022-04-23 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_token_pixiu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='symbol',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
