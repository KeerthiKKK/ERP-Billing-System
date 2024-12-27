# Generated by Django 5.1.4 on 2024-12-27 14:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billingapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_title', models.CharField(blank=True, max_length=100, null=True)),
                ('business_address', models.TextField(blank=True, max_length=400, null=True)),
                ('business_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('business_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('business_gst', models.CharField(blank=True, max_length=15, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]