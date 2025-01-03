# Generated by Django 5.1.4 on 2024-12-29 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billingapp', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_address', models.TextField()),
                ('customer_mobileno', models.IntegerField()),
                ('customer_gst', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='billing',
            name='bill_address',
        ),
        migrations.RemoveField(
            model_name='billing',
            name='bill_amount',
        ),
        migrations.RemoveField(
            model_name='billing',
            name='bill_items',
        ),
    ]
