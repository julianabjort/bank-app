# Generated by Django 4.0.3 on 2022-05-12 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0007_alter_customer_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='balance',
        ),
    ]
