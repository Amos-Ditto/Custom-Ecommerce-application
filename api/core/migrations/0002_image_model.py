# Generated by Django 3.2.12 on 2022-03-07 19:33

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='image_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('alt', models.TextField(null=True)),
                ('image', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/images'), upload_to='')),
            ],
        ),
    ]