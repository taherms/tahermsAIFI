# Generated by Django 3.1.6 on 2021-02-09 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]