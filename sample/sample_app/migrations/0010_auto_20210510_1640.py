# Generated by Django 2.2.4 on 2021-05-10 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0009_auto_20210509_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliv_form',
            name='auction_status',
            field=models.CharField(default='live', max_length=30),
        ),
    ]
