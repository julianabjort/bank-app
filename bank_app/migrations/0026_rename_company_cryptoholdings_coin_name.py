# Generated by Django 4.0.5 on 2022-06-08 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0025_alter_cryptoholdings_shares'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cryptoholdings',
            old_name='company',
            new_name='coin_name',
        ),
    ]