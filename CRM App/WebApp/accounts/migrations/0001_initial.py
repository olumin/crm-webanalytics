# Generated by Django 5.0.1 on 2024-02-06 09:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('elements', models.CharField(max_length=50)),
                ('partners_name', models.CharField(max_length=50)),
                ('products', models.CharField(max_length=50)),
                ('current_focus', models.CharField(max_length=50)),
                ('actual', models.CharField(max_length=50)),
                ('achieved', models.CharField(max_length=50)),
                ('points', models.CharField(max_length=50)),
                ('commission', models.CharField(max_length=50)),
                ('next_airtime_expectation', models.CharField(max_length=50)),
                ('topit_expectation', models.CharField(max_length=50)),
                ('topit_focus', models.CharField(max_length=50)),
                ('topit_actual', models.CharField(max_length=50)),
                ('topit_achieved', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50, null=True)),
                ('currentmonth', models.CharField(max_length=50, null=True)),
                ('monthsec', models.CharField(max_length=50, null=True)),
                ('total_airtime', models.CharField(max_length=50)),
                ('total_topit', models.CharField(max_length=50)),
                ('total_commission', models.CharField(max_length=50)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Score_hist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('elements', models.CharField(max_length=50)),
                ('products', models.CharField(max_length=50)),
                ('current_focus', models.FloatField()),
                ('actual', models.FloatField()),
                ('achieved', models.FloatField()),
                ('point', models.FloatField()),
                ('commission', models.FloatField()),
                ('next_airtime_expectation', models.FloatField()),
                ('topit_expectation', models.FloatField()),
                ('topit_focus', models.CharField(max_length=50)),
                ('topit_actual', models.CharField(max_length=50)),
                ('topit_achieved', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50, null=True)),
                ('currentmonth', models.CharField(max_length=50, null=True)),
                ('monthsec', models.CharField(max_length=50, null=True)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
