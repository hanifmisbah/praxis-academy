# Generated by Django 2.2 on 2020-09-08 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud1', '0004_auto_20200904_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='dev',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='game',
            name='year',
            field=models.CharField(max_length=20),
        ),
    ]
