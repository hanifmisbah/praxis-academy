# Generated by Django 2.2 on 2020-09-03 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('genre', models.TextField(default='')),
                ('year', models.TextField(default='')),
                ('dev', models.TextField(default='')),
            ],
        ),
    ]
