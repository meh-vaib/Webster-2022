# Generated by Django 4.1.5 on 2023-03-07 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='repassword',
        ),
    ]