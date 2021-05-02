# Generated by Django 2.2.4 on 2021-04-26 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30, unique=True)),
                ('age', models.IntegerField()),
                ('email_id', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]