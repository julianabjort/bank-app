# Generated by Django 4.0.3 on 2022-06-06 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0018_alter_account_account_type_accountrequest'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AccountRequest',
        ),
    ]
