# Generated by Django 4.0.3 on 2023-11-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_variation_name_variation_variation_value'),
        ('carts', '0002_rename_cartition_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]
