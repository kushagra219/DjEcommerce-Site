# Generated by Django 2.2.10 on 2020-03-16 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_order_billing_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billingaddress',
            old_name='countries',
            new_name='country',
        ),
    ]
