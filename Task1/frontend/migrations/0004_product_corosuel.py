# Generated by Django 3.1.6 on 2021-02-09 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_product_bestsellers'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='corosuel',
            field=models.BooleanField(default=False),
        ),
    ]