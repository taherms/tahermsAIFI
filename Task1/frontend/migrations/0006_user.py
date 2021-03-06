# Generated by Django 3.1.6 on 2021-02-09 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_remove_product_corosuel'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contact', models.TextField()),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateField()),
            ],
        ),
    ]
