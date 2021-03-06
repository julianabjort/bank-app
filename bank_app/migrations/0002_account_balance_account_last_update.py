# Generated by Django 4.0.3 on 2022-05-09 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='last_update',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
