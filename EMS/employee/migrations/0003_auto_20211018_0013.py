# Generated by Django 3.1 on 2021-10-17 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20211018_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone_no',
            field=models.PositiveIntegerField(max_length=10),
        ),
    ]
