# Generated by Django 5.0.7 on 2024-07-20 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShopManage.city')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('house', models.IntegerField()),
                ('opening', models.TimeField(blank=True)),
                ('closing', models.TimeField(blank=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShopManage.city')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShopManage.street')),
            ],
        ),
    ]
