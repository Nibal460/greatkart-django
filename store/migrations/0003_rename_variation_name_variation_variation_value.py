# Generated by Django 4.0.3 on 2023-11-23 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='variation_name',
            new_name='variation_value',
        ),
    ]