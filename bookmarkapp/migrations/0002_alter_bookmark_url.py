# Generated by Django 3.2.5 on 2021-07-26 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarkapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='url',
            field=models.URLField(verbose_name='url'),
        ),
    ]
