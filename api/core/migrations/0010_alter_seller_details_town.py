# Generated by Django 3.2.12 on 2022-05-17 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_products_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller_details',
            name='town',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
