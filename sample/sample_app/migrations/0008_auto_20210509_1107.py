# Generated by Django 2.2.4 on 2021-05-09 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0007_bid_table_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid_table',
            name='deliv_form_id',
            field=models.CharField(max_length=30),
        ),
    ]
