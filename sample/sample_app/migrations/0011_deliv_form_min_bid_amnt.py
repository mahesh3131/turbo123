# Generated by Django 2.2.4 on 2021-05-13 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0010_auto_20210510_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliv_form',
            name='min_bid_amnt',
            field=models.IntegerField(default=200),
            preserve_default=False,
        ),
    ]