# Generated by Django 3.1.7 on 2021-04-05 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210405_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
