# Generated by Django 4.0.3 on 2022-05-18 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0013_alter_ledger_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledger',
            name='text',
            field=models.TextField(default='text'),
        ),
    ]
