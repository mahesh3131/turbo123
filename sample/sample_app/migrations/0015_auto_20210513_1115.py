# Generated by Django 2.2.4 on 2021-05-13 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0014_bid_table_deliv_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliv_form',
            name='min_bid_amnt',
            field=models.IntegerField(default=0),
        ),
    ]
