# Generated by Django 4.0.4 on 2022-04-27 16:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='daily_bill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bill_key', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('bill_value', models.JSONField()),
                ('status', models.CharField(blank=True, max_length=32, null=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lp',
            fields=[
                ('symbol', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('isLp', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('decimals', models.IntegerField(blank=True, default=0, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('symbol', models.CharField(blank=True, max_length=50, null=True)),
                ('logo_url', models.CharField(blank=True, max_length=150, null=True)),
                ('address', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('update_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('quote_currency', models.CharField(blank=True, max_length=20, null=True)),
                ('pixiu', models.BooleanField(blank=True, null=True)),
                ('isLp', models.BooleanField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('address', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Trans',
            fields=[
                ('blockNumber', models.IntegerField(blank=True, default=0, null=True)),
                ('hash', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('blockHash', models.CharField(max_length=50, unique=True)),
                ('fromAddr', models.CharField(max_length=50, unique=True)),
                ('toAddr', models.CharField(max_length=50, unique=True)),
                ('value', models.IntegerField(blank=True, default=0, null=True)),
                ('Token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.token')),
            ],
        ),
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('price', models.FloatField(blank=True, default=0, null=True)),
                ('Token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.token')),
            ],
        ),
    ]
